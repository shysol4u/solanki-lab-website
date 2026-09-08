# Version 6 launch status

**Public GitHub Pages launch verified on 2026-09-08.** The website is live at [https://shysol4u.github.io/solanki-lab-website/](https://shysol4u.github.io/solanki-lab-website/). GitHub `main` is now the master source. The approved website is unchanged. **The requested final address, `https://solankilab.org`, is pending registration and DNS connection; it is not live at that address yet.** Phone/tablet visual testing remains unverified; the limits below are explicit.

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
| Requested `solankilab.org` | Owner requested this final domain on 2026-09-08; registry lookup returned no registration record and DNS returned NXDOMAIN. Registration, owner control, DNS, and custom-domain HTTPS remain pending |

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

Future documentation-only commits may advance `main` and rerun the same deployment workflow. The launch release tag above remains fixed. No domain, plan, paid runner, trial, analytics product, or account subscription has been purchased or activated.
