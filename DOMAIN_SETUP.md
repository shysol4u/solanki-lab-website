# Connect solankilab.org

The owner requested **https://solankilab.org** as the final website address on 2026-09-08 and purchased the domain from Porkbun on 2026-09-09. The approved Version 6 website uses free GitHub Pages.

## Current status

On 2026-09-09, Public Interest Registry RDAP confirmed registration with Porkbun LLC at 02:55:27 UTC, expiring on 2027-09-09. The signed-in owner's Porkbun account also lists `solankilab.org`. This supersedes the pre-registration observations from 2026-09-08.

**Connection verified on 2026-09-09: https://solankilab.org/.** GitHub account ownership verification succeeded. The TXT verification record is saved at Porkbun and publicly resolves. The repository's Pages custom domain is `solankilab.org`. Public DNS returns all four GitHub A records and the `www` CNAME below. The original apex `ALIAS` to `pixie.porkbun.com` was replaced, and public wildcard CNAME queries now return NXDOMAIN, confirming removal of the default parking wildcard.

The configuration uses `site_url: https://solankilab.org` and `custom_domain_approved: true`. All seven page bodies and 50 approved non-HTML files are unchanged after rebuilding. The deployment succeeded, all 60 public files returned HTTP 200 with exact expected bytes over HTTPS, and HTTP, `www`, and the original GitHub URL return permanent redirects to the secure final address. GitHub's **Enforce HTTPS** setting is checked and persists after reloading. See `audit/domain-check.json`, `audit/deployment-check.json`, and `LAUNCH_STATUS.md`.

## Recreating or maintaining the connection

1. Confirm the existing owner-controlled Porkbun registration. The domain is already purchased. Preserve its registration and the existing nameservers; no hosting, email, premium DNS, or SSL add-on is required for this website.
2. Verify domain ownership in the `shysol4u` GitHub account using the TXT record GitHub supplies. Keep that verification record in DNS.
3. Add `solankilab.org` in this repository’s **Settings → Pages → Custom domain** before pointing its web DNS records at GitHub Pages.
4. Apply the web DNS records below, preserving unrelated records. Use `www` as an alias for the apex domain.
5. Wait for GitHub’s DNS check and certificate provisioning, enable **Enforce HTTPS**, and verify that `www.solankilab.org` redirects to `https://solankilab.org`.
6. Set `site_url` to `https://solankilab.org` and `custom_domain_approved` to true. Rebuild the generated metadata, sitemap, and robots file; preserve all seven approved page bodies and all 50 approved non-HTML files. Run the documented build and checks.
7. Commit the domain metadata change, verify the successful deployment, and run `python3 scripts/verify-deployment.py https://solankilab.org/`. Recheck every route and asset, the apex/www redirects, and the real browser appearance. Update launch/domain records only with observed results.

## DNS values checked against GitHub documentation on 2026-09-09

| Type | Name | Value |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `shysol4u.github.io` |
| TXT | `_github-pages-challenge-shysol4u` | `858138948448037329da0c5b9dc858` |

All six configured records use a 600-second TTL at Porkbun. Retain the ownership TXT record. The existing Porkbun nameservers remain unchanged; no email records were present when configuration began.

The CNAME target contains no repository path. Do not create wildcard records. The current custom Actions workflow does not require a CNAME file in the uploaded site; the repository’s Pages settings hold the domain configuration. DNS and certificate provisioning can require additional time; verify readiness instead of assuming it.

[GitHub’s official custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
