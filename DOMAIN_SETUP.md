# Connect solankilab.org

The owner requested **https://solankilab.org** as the final website address on 2026-09-08. This connection is part of the current task. The approved Version 6 website is already live on free GitHub Pages at https://shysol4u.github.io/solanki-lab-website/.

## Current status

On 2026-09-08, the Public Interest Registry RDAP lookup returned HTTP 404, “Object not found,” for `solankilab.org`. Public A, NS, and MX queries returned NXDOMAIN. These observations indicate the domain is not currently registered/delegated; a registrar must confirm availability and the final checkout price. See `audit/domain-check.json`.

No domain has been purchased or connected. `AGENTS.md` requires explicit owner approval for any domain purchase. Registration and the registrar account must remain under the owner’s control. GitHub Pages hosting and its HTTPS certificate remain free.

Keep the working GitHub Pages `site_url` and Pages settings active until the owner controls the domain. The existing `preferred_domain` already names `solankilab.org`; activation is pending, and `custom_domain_approved` remains false until ownership is established.

## Prepared connection sequence

1. Obtain the owner’s approval for the actual registration cost and register `solankilab.org` in the owner’s account, or confirm an existing owner-controlled registration. Do not buy hosting, email, premium DNS, SSL, or other add-ons.
2. Verify domain ownership in the `shysol4u` GitHub account using the TXT record GitHub supplies. Keep that verification record in DNS.
3. Add `solankilab.org` in this repository’s **Settings → Pages → Custom domain** before pointing its web DNS records at GitHub Pages.
4. Apply the web DNS records below, preserving unrelated records. Use `www` as an alias for the apex domain.
5. Wait for GitHub’s DNS check and certificate provisioning, enable **Enforce HTTPS**, and verify that `www.solankilab.org` redirects to `https://solankilab.org`.
6. Set `site_url` to `https://solankilab.org` and `custom_domain_approved` to true. Rebuild the generated metadata, sitemap, and robots file; preserve all seven approved page bodies and all 50 approved non-HTML files. Run the documented build and checks.
7. Commit the domain metadata change, verify the successful deployment, and run `python3 scripts/verify-deployment.py https://solankilab.org/`. Recheck every route and asset, the apex/www redirects, and the real browser appearance. Update launch/domain records only with observed results.

## DNS values checked against GitHub documentation on 2026-09-08

| Type | Name | Value |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `shysol4u.github.io` |
| TXT | GitHub-provided verification name | GitHub-provided verification value |

The CNAME target contains no repository path. Do not create wildcard records. The current custom Actions workflow does not require a CNAME file in the uploaded site; the repository’s Pages settings hold the domain configuration. DNS and certificate provisioning can require additional time; verify readiness instead of assuming it.

[GitHub’s official custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
