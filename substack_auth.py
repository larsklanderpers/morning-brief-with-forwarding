#!/usr/bin/env python3
"""
Substack Session Cookie Setup
------------------------------
Grabs your Substack session cookie from Chrome and saves it to config.json.
Run this once (and again if posting starts failing with 401 errors).

Usage:
    python substack_auth.py
"""

import json
import os
import sys
import sqlite3
import shutil
import tempfile
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def get_cookie_from_chrome():
    """Try to read substack.sid from Chrome's cookie database on Windows."""
    cookie_path = Path(os.environ.get("LOCALAPPDATA", "")) / \
        "Google" / "Chrome" / "User Data" / "Default" / "Network" / "Cookies"

    if not cookie_path.exists():
        # Try Edge as fallback
        cookie_path = Path(os.environ.get("LOCALAPPDATA", "")) / \
            "Microsoft" / "Edge" / "User Data" / "Default" / "Network" / "Cookies"

    if not cookie_path.exists():
        return None

    # Copy to temp (Chrome locks the file while running)
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    try:
        shutil.copy2(cookie_path, tmp.name)
        conn = sqlite3.connect(tmp.name)
        cursor = conn.execute(
            "SELECT encrypted_value FROM cookies WHERE host_key LIKE '%substack.com' AND name='substack.sid'"
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            # encrypted_value needs DPAPI decryption on Windows — return raw bytes as signal
            return row[0]
    except Exception:
        pass
    finally:
        os.unlink(tmp.name)
    return None


def decrypt_chrome_cookie(encrypted_value):
    """Decrypt Chrome cookie value using Windows DPAPI + AES-256-GCM."""
    try:
        import base64
        import json as _json
        # Read Chrome's Local State for the encryption key
        local_state_path = Path(os.environ.get("LOCALAPPDATA", "")) / \
            "Google" / "Chrome" / "User Data" / "Local State"
        with open(local_state_path) as f:
            local_state = _json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        # Strip DPAPI prefix ("DPAPI")
        encrypted_key = encrypted_key[5:]

        import ctypes
        import ctypes.wintypes

        class DATA_BLOB(ctypes.Structure):
            _fields_ = [("cbData", ctypes.wintypes.DWORD), ("pbData", ctypes.POINTER(ctypes.c_char))]

        p = ctypes.create_string_buffer(encrypted_key, len(encrypted_key))
        blobin = DATA_BLOB(ctypes.sizeof(p), p)
        blobout = DATA_BLOB()
        ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout)
        )
        key = ctypes.string_at(blobout.pbData, blobout.cbData)

        # Decrypt the cookie value (v10 prefix = AES-256-GCM)
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        enc = bytes(encrypted_value)
        # v10 prefix is 3 bytes, then 12-byte nonce, then ciphertext
        nonce = enc[3:15]
        ciphertext = enc[15:]
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ciphertext, None).decode("utf-8")
    except ImportError:
        return None  # cryptography package not installed
    except Exception:
        return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-cookies", action="store_true",
                        help="Paste the full Cookie header string from DevTools (recommended)")
    args = parser.parse_args()

    config = load_config()

    print("=" * 60)
    print("  Substack Auth Setup")
    print("=" * 60)
    print()

    if args.full_cookies or config.get("substack", {}).get("cookie_string"):
        _setup_full_cookies(config)
    else:
        _setup_session_cookie(config)


def _setup_full_cookies(config):
    """Paste the full Cookie header — includes substack.lli JWT + cf_clearance."""
    current = config.get("substack", {}).get("cookie_string", "")
    if current:
        print(f"  Current cookie string set ({len(current)} chars).")
        replace = input("  Replace it? (y/N): ").strip().lower()
        if replace != "y":
            print("  No changes made.")
            return

    print()
    print("  FULL COOKIE METHOD (required for Cloudflare-protected endpoints)")
    print()
    print("  1. Open Chrome and go to your Substack publication")
    print("  2. Press F12 → Network tab → filter by 'api'")
    print("  3. Click any /api/v1/drafts request")
    print("  4. Under Request Headers, find the 'Cookie' row")
    print("  5. Right-click the value → Copy value")
    print("  6. Paste it below")
    print()
    cookie_string = input("  Paste full Cookie header value: ").strip()

    if not cookie_string:
        print("  ❌ Nothing pasted. Exiting.")
        sys.exit(1)

    if "substack" not in config:
        config["substack"] = {}
    config["substack"]["cookie_string"] = cookie_string
    save_config(config)
    print()
    print("  ✅ Full cookie string saved to config.json")
    print()
    print("  You can now run:")
    print('  python briefing_agent.py --substack-file "Substack Drafts\\your-draft.md"')
    print()
    print("  ⚠️  cf_clearance cookies expire after ~30 minutes.")
    print("     Re-run this script if posting starts failing.")


def _setup_session_cookie(config):
    """Legacy: save just the substack.sid cookie."""
    current = config.get("substack", {}).get("session_cookie", "")
    if current:
        print(f"  Current cookie: {current[:20]}...{current[-10:]}")
        replace = input("  Cookie already set. Replace it? (y/N): ").strip().lower()
        if replace != "y":
            print("  No changes made.")
            return

    print()
    print("  Attempting to read cookie from Chrome...")
    encrypted = get_cookie_from_chrome()
    cookie = None

    if encrypted:
        cookie = decrypt_chrome_cookie(encrypted)
        if cookie:
            print(f"  ✅ Found and decrypted: {cookie[:20]}...")
        else:
            print("  ⚠️  Found cookie but couldn't decrypt automatically.")
            print("     (Install 'cryptography' package: pip install cryptography --break-system-packages)")
    else:
        print("  Could not read from Chrome automatically.")

    if not cookie:
        print()
        print("  MANUAL METHOD:")
        print()
        print("  1. Open Chrome and go to: https://substack.com")
        print("  2. Make sure you're logged in")
        print("  3. Press F12 → Application → Cookies → https://substack.com")
        print("  4. Find 'substack.sid' and copy its Value")
        print()
        cookie = input("  Paste the substack.sid value here: ").strip()

    if not cookie:
        print("  ❌ No cookie provided. Exiting.")
        sys.exit(1)

    # Validate
    pub_url = config.get("substack", {}).get("publication_url", "")
    if pub_url and "YOUR_HANDLE" not in pub_url:
        print()
        print("  Validating cookie...")
        import urllib.request
        try:
            req = urllib.request.Request(
                "https://substack.com/api/v1/me",
                headers={"Cookie": f"substack.sid={cookie}", "User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                me = json.loads(resp.read())
                name = me.get("name") or me.get("email", "unknown")
                print(f"  ✅ Logged in as: {name}")
        except Exception as e:
            print(f"  ⚠️  Validation failed: {e}")
            print("     Cookie saved anyway.")

    if "substack" not in config:
        config["substack"] = {}
    config["substack"]["session_cookie"] = cookie
    save_config(config)
    print()
    print("  ✅ Cookie saved to config.json")
    print()
    print("  NOTE: If you get 403 errors, run with --full-cookies instead:")
    print("  python substack_auth.py --full-cookies")


if __name__ == "__main__":
    main()
