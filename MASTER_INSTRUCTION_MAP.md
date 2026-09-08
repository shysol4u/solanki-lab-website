# Master instruction map

This map follows the 45 numbered sections of the supplied master technical instructions. **Public GitHub Pages deployment and exact HTTPS comparison are verified as of 2026-09-08. Desktop browser checks passed; phone/tablet visual testing and other limits remain explicitly recorded in `LAUNCH_STATUS.md`.** The source master document stays in the private backup.

| Section | Implementation / evidence | Status |
| --- | --- | --- |
| 1. Preserve the approved website | Immutable `approved-v6` baseline; seven page-body hashes and 50 non-HTML file hashes match | Passed source comparison |
| 2. Take technical ownership | Retain static HTML/CSS/JavaScript and the existing Python generator | Implemented |
| 3. Zero-cost hosting and deployment | Public GitHub Pages; standard Ubuntu Actions; no paid application service | Active and verified; original standard-runner workflow succeeded |
| 4. GitHub Pages adaptation | Existing relative links work under the project path; no framework migration | Passed source checks |
| 5. Alternative hosting | No alternative needed for this static architecture | Not needed |
| 6. Cost control | No purchases, subscriptions, paid runners, or spending increases | Applied |
| 7. Custom domain | Owner requested `https://solankilab.org`; `DOMAIN_SETUP.md` contains the prepared connection settings | Registry record absent; registration and DNS connection pending |
| 8. Minimal user intervention | Owner connection confirmed; launch completed with the approved package | GitHub connection and browser sign-in completed |
| 9. GitHub master copy | Target owner `shysol4u`, repository `solanki-lab-website`, branch `main` | Uploaded; main is the master source |
| 10. Complete editable source | Generator, Guidelines DOCX, CSS, JavaScript, all assets, generated HTML, workflow | Included |
| 11. Repository documentation | README, maintenance guide, changelog, asset inventory, ignore rules | Included |
| 12. README.md | Actual architecture, setup, build, preview, upload, deployment, editing, dependencies | Included |
| 13. WEBSITE_MAINTENANCE.md | Existing content variables, sections, files, and maintenance procedure | Included |
| 14. Easy content modification | Retain centralized content in `scripts/build-pages.py`; keep animation code separate | Preserved/documented |
| 15. CHANGELOG.md | Existing Versions 1–6 plus technical release `v6.0.0` | Included |
| 16. Version control | Main branch, immutable baseline and release tags; future substantial work on branches | Public history, both tags, and rollback branch confirmed |
| 17. Automatic deployment | Push to main builds, validates, and deploys; pull requests only validate | Successful real build and deployment |
| 18. Future ChatGPT maintenance | `AGENTS.md` requires latest repository inspection and targeted changes | Included |
| 19. Future request example | Maintenance guide explains how to locate, edit, build, inspect, and publish an authorized change | Included |
| 20. Long-term independence | Portable source ZIP and Git bundles; no reliance on the original chat for builds | Included |
| 21. Copyright | Scoped `COPYRIGHT.md`, served notice, and head metadata; visible approved footer retained | Included |
| 22. Lab original content | Notice limited to rights held by the lab/authors | Included |
| 23. SDSU material | University rights/trademarks excluded from lab ownership claims | Recorded |
| 24. Published scientific figures | Existing supplied figures preserved; unspecified permissions/required credits not invented | Inventory complete; rights unverified where unspecified |
| 25. Third-party assets | Existing flags, fonts, and supplied imagery listed with evidence and limitations | Recorded |
| 26. ASSET_SOURCES.md | 37 mapped media derivatives plus brand, Guidelines, flags, fonts, and code | Included |
| 27. Lab logo | Exact approved PNG/favicon plus original supplied TIFF in private backup | Preserved |
| 28. High-resolution originals | Supplied originals kept at their available resolutions; SVG wrapper also retained | Preserved; see backup note |
| 29. Privacy and security | Clean public history excludes private instruction documents and master backups; no credentials added | Checked |
| 30. .gitignore | Credentials, private backups, caches, keys, and local environment files excluded | Included |
| 31. Accessibility | Existing semantic content, focus and reduced-motion behavior preserved; code/image checks | Source checks and desktop menu/Escape checks passed; device and full accessibility testing not claimed |
| 32. Performance | Roughly 19 MB total static site; no new visual assets, runtime services, or animation dependencies | Size and desktop rendering checked; formal performance benchmark not performed |
| 33. Discoverability | Existing titles/descriptions retained; nonvisual canonical/social metadata, sitemap, robots | Added |
| 34. No hidden dependencies | Python/Node development requirements and Google Fonts runtime dependency documented | Included |
| 35. Analytics | None added | Applied |
| 36. Backups | Source ZIP, original-media backup, original Versions 1–6 Git bundle, launch Git bundle | Existing source ZIP and private history/asset bundles retained; public tags confirmed |
| 37. Pre-launch quality control | Build, content, internal links, assets, script syntax, simulated menus/orbits | Local, public HTTPS, and desktop checks passed; device QA limits recorded |
| 38. Deployed comparison | Exact original-source comparison passed; served-byte verification script ready | All 60 served files match exactly over HTTPS |
| 39. Repair and rollback | `BACKUPS.md` documents reverting and recovery without destroying history | Included |
| 40. Domain ownership | Owner-controlled GitHub confirmed; requested domain must be registered in the owner’s registrar account | Domain purchase approval and registration pending |
| 41. Make the website live | Repository created, complete source imported, Pages/HTTPS active, public and desktop checks recorded | GitHub Pages address verified; requested custom domain pending |
| 42. Definition of finished | Successful GitHub Pages launch is supported by workflow/HTTPS evidence; final domain and remaining QA limits are explicit | GitHub Pages launch verified; solankilab.org connection remains open |
| 43. Future AI maintenance rule | Latest repository first; no reconstruction from memory; targeted updates | Included in AGENTS.md |
| 44. Long-term model | Owner GitHub master → checked main updates → free Pages → requested solankilab.org | GitHub/Pages operational; domain pending |
| 45. Final operating principle | Exact approved site retained; verification limits and remaining domain work documented | GitHub launch complete; domain registration approval/control needed |

Detailed source, HTTPS, and browser evidence is in `audit/latest-check.json`, `audit/deployment-check.json`, and `audit/browser-check.json`. `LAUNCH_STATUS.md` records the public launch and remaining QA limitations. Static checks and simulated interactions are not described as real device verification.
