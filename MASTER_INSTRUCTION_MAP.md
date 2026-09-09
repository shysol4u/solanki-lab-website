# Master instruction map

This map follows the 45 numbered sections of the supplied master technical instructions. **The requested https://solankilab.org domain, free GitHub Pages deployment, and exact HTTPS comparison are verified as of 2026-09-09. Desktop browser checks passed; phone/tablet visual testing and other limits remain explicitly recorded in `LAUNCH_STATUS.md`.** The source master document stays in the private backup.

| Section | Implementation / evidence | Status |
| --- | --- | --- |
| 1. Preserve the approved website | Immutable `approved-v6` baseline; seven page-body hashes and 50 non-HTML file hashes match | Passed source comparison |
| 2. Take technical ownership | Retain static HTML/CSS/JavaScript and the existing Python generator | Implemented |
| 3. Zero-cost hosting and deployment | Public GitHub Pages; standard Ubuntu Actions; no paid application service | Active and verified; original standard-runner workflow succeeded |
| 4. GitHub Pages adaptation | Existing relative links work under the project path; no framework migration | Passed source checks |
| 5. Alternative hosting | No alternative needed for this static architecture | Not needed |
| 6. Cost control | Owner purchased the domain separately; hosting/deployment remain free, with no paid runners or added subscriptions | Applied |
| 7. Custom domain | Owner purchased `solankilab.org` at Porkbun; GitHub ownership, apex/www DNS, enforced HTTPS, redirects, and exact public bytes verified | Complete |
| 8. Minimal user intervention | Owner connection confirmed; launch completed with the approved package | GitHub connection and browser sign-in completed |
| 9. GitHub master copy | Target owner `shysol4u`, repository `solanki-lab-website`, branch `main` | Uploaded; main is the master source |
| 10. Complete editable source | Generator, Guidelines DOCX, CSS, JavaScript, all assets, generated HTML, workflow | Included |
| 11. Repository documentation | README, maintenance guide, changelog, asset inventory, ignore rules | Included |
| 12. README.md | Actual architecture, setup, build, preview, upload, deployment, editing, dependencies | Included |
| 13. WEBSITE_MAINTENANCE.md | Existing content variables, sections, files, and maintenance procedure | Included |
| 14. Easy content modification | Retain centralized content in `scripts/build-pages.py`; keep animation code separate | Preserved/documented |
| 15. CHANGELOG.md | Existing Versions 1–6, initial launch `v6.0.0`, and custom-domain launch `v6.0.1` | Included |
| 16. Version control | Main branch, immutable baseline and release tags; future substantial work on branches | Original tags/rollback branch retained; `v6.0.1` confirms the custom-domain release |
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
| 40. Domain ownership | Owner-controlled GitHub and Porkbun registration confirmed; GitHub DNS TXT verification succeeded | Verified 2026-09-09; retain the TXT record |
| 41. Make the website live | Repository created, complete source imported, Pages/HTTPS active, public and desktop checks recorded | Live at https://solankilab.org/ |
| 42. Definition of finished | Successful custom-domain launch supported by workflow, DNS, HTTPS, redirects, exact bytes, and desktop evidence | Deployment complete; remaining device QA limits explicitly retained |
| 43. Future AI maintenance rule | Latest repository first; no reconstruction from memory; targeted updates | Included in AGENTS.md |
| 44. Long-term model | Owner GitHub master → checked main updates → free Pages → solankilab.org | Operational and verified |
| 45. Final operating principle | Exact approved site retained; deployment evidence, rollback, and QA limits documented | Requested custom-domain launch complete |

Detailed source, HTTPS, and browser evidence is in `audit/latest-check.json`, `audit/deployment-check.json`, and `audit/browser-check.json`. `LAUNCH_STATUS.md` records the public launch and remaining QA limitations. Static checks and simulated interactions are not described as real device verification.
