# Version 6 launch status

**Live at [https://solankilab.org/](https://solankilab.org/); custom-domain deployment verified on 2026-09-09.** GitHub `main` is the master source and the approved Version 6 website is unchanged. The owner controls the Porkbun registration; GitHub ownership, DNS, enforced HTTPS, permanent redirects, successful deployment, and exact served-file comparisons are verified. Phone/tablet visual testing remains unverified.

## Custom-domain launch evidence — 2026-09-09

- Production website commit: `2588a38a8ee313079888d9a09c02a94d1a9ee03a`; changes only domain publishing metadata and its check/changelog records. The owner's intervening README edits are preserved.
- [Successful custom-domain workflow](https://github.com/shysol4u/solanki-lab-website/actions/runs/34346389956); the original free GitHub Actions workflow is unchanged.
- [Version 6.0.1 release](https://github.com/shysol4u/solanki-lab-website/releases/tag/v6.0.1) points to the verified website commit above. `approved-v6`, `v6.0.0`, and `rollback/approved-v6` remain unchanged.
- All 60 public files return HTTP 200 at `https://solankilab.org/` and match the expected bytes exactly. All seven approved page bodies and 50 approved non-HTML files still match the immutable Version 6 baseline.
- GitHub's DNS check succeeds and **Enforce HTTPS** is enabled. HTTP, HTTP/HTTPS `www`, and the original GitHub Pages address each return HTTP 301 to `https://solankilab.org/`.
- Ownership TXT and apex/www DNS records are verified. The default wildcard parking record is absent in public DNS.
- All seven pages opened in desktop Chrome at the final domain with correct canonical URLs and no horizontal overflow. Homepage and native Guidelines appearance, Research menu/Escape, pause/resume, and Guidelines contents were checked in the real browser.
- Detailed evidence: `audit/deployment-check.json`, `audit/domain-check.json`, `audit/browser-check.json`, and `audit/latest-check.json`.

## Initial launch evidence — 2026-09-08

The following table preserves the initial GitHub launch record. The custom-domain verification above supersedes its original URL.

| Requirement | Verified result |
| --- | --- |
| Owner and repository | Connected as `shysol4u`; public `shysol4u/solanki-lab-website` created after confirming it did not exist |
| Latest approved Version 6 | Original Sites source commit `514b4159a6010d538970bb60e53f2bc048708560` retained in the private history |
| Exact visible website | All seven HTML bodies and 50 approved non-HTML files unchanged; 3,978 preservation/content checks passed |
| Complete editable source | All 92 package files imported; tree `dc63f5092fa1b98fe69049f2b61edc340eb4f142` exactly matches the prepared ZIP and original launch repository |
| Production source | `main`; imported launch commit `6ecab33eeebb178cd31f1535d13405381bbac984` |
| Automatic free deployment | Original `.github/workflows/pages.yml` succeeded on standard Ubuntu runners; Pages source is GitHub Actions |
| Public HTTPS | Enforced for the default Pages domain; all 60 public files returned HTTP 200 and exact expected bytes |
| Local content and links | Seven pages, 356 local references, and all 183 meaningful Guidelines blocks checked |
| Navigation and animation source checks | JavaScript syntax and the documented simulated navigation/orbit checks passed |
| Real desktop browser | All seven pages opened in Chrome at 1348 px; homepage and Guidelines visually inspected; dropdowns, Escape, pause/resume controls, and Guidelines section navigation checked |
| Phone/tablet visual checks | Not completed; browser policy blocked the responsive test harness. Existing source-level responsive checks pass, but are not described as device testing |
| Rollback | `approved-v6` → `e41091e276009d656c0e5a8cb68e900ad5e576ec`; `v6.0.0` → `6ecab33eeebb178cd31f1535d13405381bbac984`; `rollback/approved-v6` branch retained |
| Original assets and Versions 1–6 | Separate private backup and original Git bundles retained; not uploaded to the public repository |
| Copyright and provenance | Existing inventory retained; unspecified third-party rights remain marked for verification |
| Requested `solankilab.org` | Completed 2026-09-09: owner-controlled registration, GitHub ownership, DNS, HTTPS, redirects, exact served files, and desktop checks verified above |

## Deployment evidence

- [Successful launch workflow](https://github.com/shysol4u/solanki-lab-website/actions/runs/34223596184), completed at approximately 11:59:59 UTC on 2026-09-08.
- `audit/deployment-check.json`: exact HTTPS comparison of all 60 served files, including all pages, scripts, styles, images, and the secondary PDF.
- `audit/browser-check.json`: actual browser checks and their limits.
- `audit/domain-check.json`: registration/DNS observations for the requested final domain; `DOMAIN_SETUP.md` contains the connection plan.
- `audit/launch-provenance.json`: source archive checksum, complete tree hashes, original/imported commit mapping, and deployment identity.
- `audit/latest-check.json`: source preservation/content evidence. The immutable `audit/approved-v6.json` is unchanged.

GitHub import commits have new IDs, while their complete file trees match the original two launch-repository commits exactly. Original commit identities and Versions 1–6 remain recoverable through the existing private bundles. No history was force-pushed.

## Remaining QA limits

Phone/tablet visual testing, physical devices, other browsers, formal performance benchmarking, and exhaustive third-party destination checks were not completed. Detailed mobile/reduced-motion/orbit behavior is supported by the existing simulated checks and unchanged source, not a claim of real device testing. These limits do not change the verified successful public deployment or exact served-byte comparison.

Future documentation-only commits may advance `main` and rerun the same deployment workflow. The launch release tag above remains fixed. The owner purchased the domain separately; GitHub Pages hosting and deployment remain free. No hosting plan, paid runner, trial, analytics product, or account subscription was added.
