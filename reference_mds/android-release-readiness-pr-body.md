## Summary

- add fail-closed, versioned Android App Bundle signing for the private pilot
- keep the development MSAL identity unchanged while generating release-only authentication configuration
- enforce distinct upload and Google Play app-signing certificate identities, with a separately named non-distributable bootstrap bundle
- cryptographically verify every AAB payload entry, its upload signer, requested version metadata, and release MSAL settings
- add CI simulations for missing, relative-path, noncanonical, upload-identity, bootstrap, and valid pilot configurations
- add a certificate-hash helper and a complete Google Play internal-testing runbook

## Verification

- `npm run build`
- `npm test` — 25 passed
- `npm run test:e2e` — 4 passed
- `:shared:testAndroidHostTest :androidApp:testDebugUnitTest :androidApp:compileDebugAndroidTestKotlin :androidApp:assembleDebug`
- release build fails closed without signing configuration
- relative upload-keystore paths are rejected
- unpadded upload and development certificate hashes are rejected
- disposable bootstrap AAB signed and verified
- disposable pilot AAB signed and verified with a distinct Play identity
- MSAL certificate helper matched an independently calculated SHA-1 hash and redirect URI
- independent code review: no remaining critical, important, or safety-relevant minor findings

## After merge

The next manual checkpoint is to create and protect Player Elite's permanent upload key, create the Play Console app with Play App Signing, add the Play signing certificate hash to Entra, and upload the verified pilot AAB to the internal test track. No real key, password, certificate hash, or release artifact is committed here.
