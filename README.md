# Solanki Lab

Functional Genomics of Plant–Microbe–Soil Interactions · South Dakota State University

This repository contains the complete editable website approved as **Version 6**, together with free GitHub Pages deployment and maintenance instructions. The migration preserves all seven visible page bodies and all 50 other approved website files. Publishing metadata, a sitemap, a robots file, and a copyright notice are the only website additions; they do not change the visible design.

**Live and verified on 2026-09-09: [solankilab.org](https://solankilab.org/).** The GitHub Pages workflow succeeded and all 60 public files match the prepared source exactly over HTTPS. HTTP, `www`, and the original GitHub address redirect to the secure final address. All seven approved page bodies and 50 approved non-HTML files remain unchanged. Desktop checks passed; phone/tablet visual testing remains unverified. See `LAUNCH_STATUS.md` for evidence and limits.

`MASTER_INSTRUCTION_MAP.md` maps all 45 instruction sections to their implementation and any remaining verification.

| Item | Configuration |
| --- | --- |
| Owner account requested by the lab | `shysol4u` |
| Repository | `shysol4u/solanki-lab-website` |
| Original free address | `https://shysol4u.github.io/solanki-lab-website/`; redirects to the configured custom domain |
| Final website address | `https://solankilab.org/`; ownership, DNS, enforced HTTPS, redirects, and deployment verified |
| Production branch | `main` |
| Hosting | GitHub Pages |
| Deployment | `.github/workflows/pages.yml` |
| Approved visual baseline | Version 6; tag `approved-v6` |
| Initial technical release | `v6.0.0`; publicly deployed and verified, with browser-testing limits in `LAUNCH_STATUS.md` |
| Custom-domain release | `v6.0.1`; verified at `https://solankilab.org/`; original rollback tags retained |

## How the site works

The browser receives ordinary HTML, CSS, and JavaScript. A small Python script generates the seven HTML pages from the existing shared templates and central content definitions. There is no React application, TypeScript compiler, npm package manager, backend, server database, API subscription, or runtime Python service.

The animations are the existing custom Canvas and browser JavaScript in `dist/universe.js` and `dist/site.js`. They do not need a third-party animation library. Keeping this architecture preserves the approved visual effects and makes the same files portable to another static host.

`dist/` is deliberately tracked. Its stylesheets, scripts, images, and PDF are authored source assets; **do not delete this directory as a build cache**. The generated HTML is also included so the approved website is immediately recoverable.

## Software and dependencies

- **Python 3.10 or newer:** builds pages and runs content/link checks using only the standard library. No `pip install` step is required.
- **Node.js 18 or newer:** runs JavaScript syntax and simulated interaction checks. No `npm install` step is required. Node is not needed by visitors.
- **Git:** maintains source and rollback history.
- **GitHub CLI, when performing initial setup from a developer's computer:** optional authenticated deployment convenience. The connected GitHub tools can perform the equivalent operations.
- **Browser-time external service:** the existing Google Fonts stylesheet supplies DM Sans and Manrope. Browser fallback fonts remain as approved. See `DEPENDENCIES.md`.
- **GitHub Actions:** official `actions/checkout@v6`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v4`, and `actions/deploy-pages@v4` on standard Ubuntu runners. No custom secrets are required by the workflow.

## Build and check locally

From the repository directory:

```bash
python -B scripts/build-pages.py
python scripts/check-site.py
node --check dist/site.js
node --check dist/universe.js
node scripts/check-navigation.cjs
node scripts/check-orbit.cjs
```

For the initial migration, also run:

```bash
python scripts/check-site.py --preserve-v6
```

That additional check proves the seven HTML bodies and all 50 other approved files match the original Version 6. Future authorized content edits can legitimately change them; do not replace the immutable baseline to disguise changes.

## Preview on your own computer

From the repository directory, run:

```bash
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:8000/` in your browser. Stop the local server with Ctrl+C. This is a preview on your own computer, not a public deployment. In an AI-managed environment, follow that environment's supported browser-preview controls instead of assuming this server can be reached by its browser.

## Where to edit

The detailed table is in `WEBSITE_MAINTENANCE.md`. Most text is centralized in `scripts/build-pages.py`; it is separate from the animation implementations. Lab Guidelines use the retained authoritative Word document and `scripts/guidelines_document.py`. Assets are indexed in three `docs/asset-map*.json` files.

After editing the source, run the build/check commands, inspect the requested change, and commit the source together with regenerated HTML. Substantial changes should be reviewed on a temporary branch before merging into `main`. An approved push to `main` then builds, checks, and publishes automatically; pull requests only build and check.

## Initial GitHub launch


1. Confirms the authenticated owner is `shysol4u` and checks whether `solanki-lab-website` already exists. Inspect and preserve an existing repository before changing it.
2. Creates a **public** repository for the free GitHub Pages path, without enabling paid products, Codespaces, LFS, or trials.
3. Pushes the complete editable source, `main`, and the approved/release tags.
4. Enables **Settings → Pages → Source: GitHub Actions**. The existing workflow supplies the build and deployment. If needed, the API equivalent is `POST /repos/shysol4u/solanki-lab-website/pages` with `build_type: workflow`; it requires appropriate repository administration and Pages permissions.
5. Runs or reruns the workflow, waits for success, and obtains the real deployment URL from GitHub.
6. Confirms public HTTPS, all routes and assets, and desktop/tablet/mobile behavior. Uses `scripts/verify-deployment.py` for byte comparison plus real browser testing for appearance and interactions.
7. Updates `LAUNCH_STATUS.md` with verified results and the final URL. Only then is GitHub the confirmed master copy and the migration complete.

GitHub Pages supports static HTML/CSS/JavaScript and is available for public repositories on GitHub Free. Standard-runner GitHub Pages workflows are free; this workflow uses a one-day Pages artifact and no build cache or additional artifacts. Keep paid runner types and spending increases disabled. See [GitHub Pages availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions).

## Domain, ownership, and backups

**https://solankilab.org** is the final website address requested on 2026-09-08. The owner purchased the domain from Porkbun on 2026-09-09. The domain is verified in the `shysol4u` GitHub account, the repository's custom domain is set, and public DNS returns GitHub's four A records and the `www` CNAME. `DOMAIN_SETUP.md` records the configuration and verification. The owner retains the registration; GitHub Pages hosting and deployment remain free.

`COPYRIGHT.md` and `ASSET_SOURCES.md` distinguish lab content, university material, and third-party assets. Unverified rights are marked; no license is guessed.

The downloadable source ZIP preserves this repository's files. A separate private backup holds the original assets, original supplied documents, and Git bundles containing earlier approved versions. Never upload the private backup to this public repository. See `BACKUPS.md` for recovery.

After initial upload, GitHub `main` is the source of truth. Update should start from the latest repository and read `AGENTS.md`, not recreate the website from memory.
