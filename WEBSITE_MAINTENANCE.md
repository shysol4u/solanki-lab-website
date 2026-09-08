# Website maintenance map

Start from the latest GitHub `main` after the initial upload is confirmed. Preserve the approved design and make only requested changes. Files below are relative to the repository root.

| Website area | Authoritative editable location | Published output / supporting assets |
| --- | --- | --- |
| Homepage introduction and sections | `scripts/build-pages.py`: `home` and `page('index.html', …)` | `dist/index.html` |
| Orbiting research theme text and destinations | `scripts/build-pages.py`: `themes` and `cards` | `dist/index.html`; motion in `dist/site.js` |
| Research page, questions, figures | `scripts/build-pages.py`: `programs`, `contents`, `research` | `dist/research.html`; `dist/assets/research/` |
| Lab-to-Land / Our Approach | `scripts/build-pages.py`: `steps`, `stephtml`, and the homepage `approach` section | `dist/index.html#approach` and existing subsection anchors |
| Team members and research descriptions | `scripts/build-pages.py`: `students`, team-generation loop, and `team` markup | `dist/team.html`; `dist/assets/team/` |
| Principal investigator, role, biography, links | `scripts/build-pages.py`: PI portion of `team` | `dist/team.html#principal-investigator` |
| Graduate student data | `scripts/build-pages.py`: central `students` list | Name, email, image key, and research biography are stored together |
| Undergraduate students, temporary staff, alumni | `scripts/build-pages.py`: corresponding sections in `team` | Existing Team-page section anchors |
| Outreach, GeN-G, GeN-G BRING, field contact, industry | `scripts/build-pages.py`: `outreach` markup and page call | `dist/outreach.html`; `dist/assets/outreach/` |
| Funding | `scripts/build-pages.py`: `funding` | `dist/funding.html` |
| Recruitment | `scripts/build-pages.py`: `recruitment` | `dist/recruitment.html` |
| Lab Guidelines wording and hierarchy | `docs/Solanki_Lab_FGPMSI_V1-source.docx`; reviewed conversion in `scripts/guidelines_document.py` | `dist/guidelines.html`; `docs/guidelines-v6-source-map.json` |
| Lab Guidelines readability styles | `dist/guidelines.css` | Loaded only by the Guidelines page |
| Secondary Guidelines PDF | `dist/files/Solanki_Lab_FGPMSI.pdf` | Regenerate from the newest approved source only when Guidelines change; preserve all meaningful pages |
| Main navigation, dropdowns, destination labels | `scripts/build-pages.py`: `menus` and `header()` | Shared across all seven pages |
| Footer and institutional contact information | `scripts/build-pages.py`: `footer` | Shared footer on all pages |
| Global colors, typography, layout, mobile breakpoints | `dist/style.css` | Keep unchanged for ordinary content updates |
| Particle universe, DNA, sequences, pointer response | `dist/universe.js` | Homepage Canvas; preserve approved drawing and motion logic |
| Orbit, pause, hover/focus, mobile menu behavior | `dist/site.js` | Shared interaction script |
| Image paths and dimensions | `docs/asset-map.json`, `docs/asset-map-v4.json`, `docs/asset-map-v5.json` | Exact asset paths under `dist/assets/` |
| Website logo and favicon | `dist/assets/brand/solanki-lab.png`, `dist/assets/brand/favicon.png` | Original supplied TIFF remains in the private asset backup |
| Guidelines source logo | `dist/assets/guidelines/solanki-lab-source-logo.png` | Lossless copy of the image in the authoritative Guidelines source |
| Page titles and descriptions | Each `page()` call in `scripts/build-pages.py` | Used consistently by existing and social metadata |
| Canonical URLs, social metadata, copyright | `scripts/publishing_metadata.py`; `site-config.json` | HTML head only; also produces sitemap, robots, and copyright files |
| Publications | No separate Publications page or dataset exists in approved Version 6 | Do not invent or add one during an unrelated update; add only if requested |
| Asset rights and required credit | `ASSET_SOURCES.md`, `COPYRIGHT.md` | Keep provenance current when assets change |
| Automated deployment | `.github/workflows/pages.yml` | Builds/checks PRs; publishes approved `main` pushes |
| Verification and baseline | `scripts/check-site.py`, `scripts/check-navigation.cjs`, `scripts/check-orbit.cjs`, `audit/approved-v6.json` | Source and simulated checks; not substitutes for browser QA |

## Typical content update

1. Fetch and inspect the current repository; create a short-lived branch for a substantial change.
2. Find the relevant central content definition using this table. Edit only that definition and any explicitly requested asset.
3. Rebuild and run the README checks. Review the changed output and confirm unrelated assets, styles, page sections, and animation scripts remain unchanged.
4. Obtain any content/visual approval the current request actually requires. If the user has already approved publishing, continue without asking again.
5. Commit a clear description of the requested change; update `CHANGELOG.md`. Merge to `main` when authorized and verify the automatic deployment.

## Replacing a portrait or figure

Keep the original file privately. Add the approved web image under the appropriate asset folder, update its central image reference/dimensions, and preserve its aspect ratio and meaningful content. Update alt text when the depicted subject changes. Do not alter another person's profile or the Team layout. Preserve original scientific figures and captions; do not use a generated replacement.

## Updating Lab Guidelines

The converter checks the source hash so it cannot silently apply an old structure map to a different Word document. Read the complete replacement document, review headings and code blocks, extract its supplied images, and update the conversion mapping/hash only after that review. Verify every meaningful source block and regenerate the secondary PDF if it is retained. Do not rebuild the policy from an old PDF or summary.

## Technical files that usually stay unchanged

Ordinary text and photograph edits should not need changes to `.github/workflows/pages.yml`, `.gitattributes`, `dist/site.js`, `dist/universe.js`, `dist/style.css`, or the page-wrapper/header helpers. Changing the domain normally affects `site-config.json`, GitHub Pages settings, and DNS only. Keep the original V6 audit baseline immutable.
