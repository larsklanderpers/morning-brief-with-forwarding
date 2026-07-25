#!/usr/bin/env python3
"""
LinkedIn OAuth 2.0 Authentication Helper
Run this once to get your access token, which is then saved to config.json.

Steps:
  1. Create a LinkedIn Developer App at https://developer.linkedin.com/
  2. Add "Share on LinkedIn" and "Sign In with LinkedIn using OpenID Connect" products
  3. Set a redirect URI of http://localhost:8888/callback
  4. Copy your Client ID and Client Secret into config.json
  5. Run: python linkedin_auth.py

The script opens a browser for you to authorize, then captures the token automatically.
"""

import json
import urllib.request
import urllib.parse
import webbrowser
import http.server
import threading
import base64
import secrets
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.json"
REDIRECT_URI = "http://localhost:8888/callback"
SCOPES = ["openid", "profile", "w_member_social"]  # w_member_social = post on behalf of member


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
    print("✅ Config updated with new tokens.")


# ── Local callback server ─────────────────────────────────────────────────────
auth_code = None
auth_event = threading.Event()


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
<html><body style="font-family:sans-serif;padding:40px;text-align:center">
<h2>&#10003; Authorization successful!</h2>
<p>You can close this tab and return to the terminal.</p>
</body></html>""")
            auth_event.set()
        else:
            error = params.get("error_description", ["Unknown error"])[0]
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"<html><body><h2>Error: {error}</h2></body></html>".encode())
            auth_event.set()

    def log_message(self, format, *args):
        pass  # Silence request logs


def start_callback_server():
    server = http.server.HTTPServer(("localhost", 8888), CallbackHandler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()
    return server


# ── OAuth flow ────────────────────────────────────────────────────────────────
def exchange_code_for_token(code, client_id, client_secret):
    url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"❌ Token exchange failed ({e.code}): {body}")
        return None


def verify_token(access_token):
    """Check the token works by fetching the user profile."""
    url = "https://api.linkedin.com/v2/me"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {access_token}")
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            name = f"{data.get('localizedFirstName', '')} {data.get('localizedLastName', '')}".strip()
            return name or data.get("id", "Unknown")
    except Exception as e:
        print(f"  [WARN] Could not verify token: {e}")
        return None


def main():
    config = load_config()
    client_id = config["linkedin"].get("client_id", "")
    client_secret = config["linkedin"].get("client_secret", "")

    if not client_id or client_id == "YOUR_CLIENT_ID":
        print("""
❌ LinkedIn credentials not configured.

Steps to get your credentials:
  1. Go to https://developer.linkedin.com/
  2. Click 'Create App'
  3. Fill in App Name (e.g. 'MorningBrief'), Company (your LinkedIn page), and Logo
  4. Under 'Products', add:
       - 'Share on LinkedIn'
       - 'Sign In with LinkedIn using OpenID Connect'
  5. Go to 'Auth' tab → copy your Client ID and Client Secret
  6. Under 'Auth' → 'OAuth 2.0 settings', add redirect URL: http://localhost:8888/callback
  7. Paste Client ID and Client Secret into config.json:
       "linkedin": {
           "client_id": "YOUR_ACTUAL_CLIENT_ID",
           "client_secret": "YOUR_ACTUAL_CLIENT_SECRET",
           ...
       }
  8. Re-run: python linkedin_auth.py
""")
        return

    # Check if we already have a valid token
    existing_token = config["linkedin"].get("access_token", "")
    if existing_token:
        print("🔑 Found existing access token. Verifying...")
        name = verify_token(existing_token)
        if name:
            print(f"✅ Token is valid. Authenticated as: {name}")
            print("   (Delete the access_token from config.json to re-authenticate)")
            return
        else:
            print("   Token expired or invalid. Re-authenticating...")

    # Build authorization URL
    state = secrets.token_urlsafe(16)
    params = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "state": state,
        "scope": " ".join(SCOPES),
    })
    auth_url = f"https://www.linkedin.com/oauth/v2/authorization?{params}"

    print("\n🔐 Starting LinkedIn OAuth flow...")
    print(f"   Opening browser for authorization...")
    print(f"   (If browser doesn't open, visit: {auth_url})\n")

    start_callback_server()
    webbrowser.open(auth_url)

    print("⏳ Waiting for authorization (you have 2 minutes)...")
    auth_event.wait(timeout=120)

    if not auth_code:
        print("❌ Authorization timed out or was cancelled.")
        return

    print("🔄 Exchanging code for access token...")
    token_data = exchange_code_for_token(auth_code, client_id, client_secret)
    if not token_data:
        return

    access_token = token_data.get("access_token", "")
    expires_in = token_data.get("expires_in", 0)

    name = verify_token(access_token)
    if name:
        print(f"✅ Successfully authenticated as: {name}")
        print(f"   Token expires in {expires_in // 3600} hours ({expires_in // 86400} days)")

    # Save to config
    config["linkedin"]["access_token"] = access_token
    config["linkedin"]["token_expiry"] = str(expires_in)
    save_config(config)

    print("\n🎉 LinkedIn is ready! You can now use:")
    print("   python briefing_agent.py --post <item_number>")


if __name__ == "__main__":
    main()
