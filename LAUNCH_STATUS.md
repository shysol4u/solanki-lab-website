# Version 6 launch status

**Prepared, but not yet published to GitHub Pages.** Owner GitHub authorization is required before the repository can be created/inspected, uploaded, and configured. The existing approved Sites copy remains unchanged. Its existing private link is not evidence of a completed public GitHub Pages launch.

| Requirement | Status |
| --- | --- |
| Latest approved Version 6 used | Complete; original source commit `514b4159a6010d538970bb60e53f2bc048708560` |
| Exact visible website preserved | Complete; all seven HTML bodies and 50 other approved files match |
| Complete editable source | Prepared, including page generator, original Guidelines source, asset maps, CSS, JavaScript, images, and PDF |
| GitHub Pages compatibility | Confirmed by static architecture, relative-link checks, and build checks |
| Free automatic deployment | Workflow prepared; activation and successful run pending GitHub access |
| Maintenance/readme/changelog | Complete |
| Copyright and asset provenance | Complete inventory; unspecified third-party ownership/licenses explicitly marked for verification |
| Original supplied assets and past versions | Preserved in the separate private backup, at their available source resolutions |
| Local content/link checks | Passed; all seven pages and 183 meaningful Guidelines blocks checked |
| Animation/navigation checks | Script syntax and simulated menu/orbit behavior checks passed; scripts remain byte-identical to Version 6 |
| Real browser/device testing | Pending; not performed by the static/simulated checks |
| Source in owner’s GitHub | Pending owner account connection |
| Public website / HTTPS / served-byte comparison | Pending actual GitHub deployment |
| `solankilab.org` | Not checked for availability/ownership, purchased, or configured; optional and subject to owner approval |

## Remaining launch actions for the maintainer

1. Use the connected GitHub account to verify `shysol4u`; inspect any existing `solanki-lab-website` repository before changes.
2. Upload the reviewed complete source and tags, configure GitHub Pages for Actions, and verify that the workflow uses standard free runners with no paid products or spending increases.
3. Wait for the actual successful deployment. Record the returned public URL, commit, and workflow/deployment status.
4. Run `python scripts/verify-deployment.py https://shysol4u.github.io/solanki-lab-website/` in a permitted network-capable environment, and perform real browser QA at representative desktop, tablet, and mobile sizes.
5. Check visual fidelity, all dropdowns, internal/external links, orbit hover/focus pause, global pause, pointer response, reduced-motion behavior, Guidelines scrolling, images, and code scrolling. Record failures and fix only migration-related discrepancies.
6. Only after those checks pass, replace the pending entries here with verified results and declare the public migration complete.

No domain, plan, paid service, analytics product, or account subscription has been purchased or activated.
