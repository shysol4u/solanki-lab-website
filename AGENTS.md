# Maintaining the Solanki Lab website

1. After the initial migration, inspect the latest `shysol4u/solanki-lab-website` repository and its `main` branch before changing anything. GitHub becomes the master source only after the initial upload is confirmed.
2. Read `README.md`, `WEBSITE_MAINTENANCE.md`, and the current user request. Preserve approved content, design, backgrounds, animations, navigation, figures, and responsive behavior outside the requested scope.
3. This is a static HTML/CSS/JavaScript site with a small Python standard-library page generator. Preserve this architecture. There is no npm installation, framework, backend, database, or paid service to set up.
4. Make substantial future changes on a temporary branch. Build and check before presenting the requested change. The user's explicit authorization to publish controls merging or deploying; do not add an unnecessary confirmation step when authorization already exists.
5. Run `python -B scripts/build-pages.py`, `python scripts/check-site.py`, and the documented Node checks. `--preserve-v6` is an initial-migration fidelity check; the immutable V6 baseline should not be rewritten to hide future intentional changes.
6. Keep all meaningful Lab Guidelines content and its original structure. A newly supplied authoritative guidelines document requires a full read and reviewed conversion map before replacing the current source/hash.
7. Keep `dist/` under version control: its CSS, JavaScript, images, and PDF are source assets, not disposable build caches. Do not delete it during a build.
8. Keep hosting and deployment at $0. Use GitHub Pages, standard GitHub-hosted runners, the one-day Pages artifact, and no paid products, paid trials, analytics, cloud databases, or LFS. Domain purchases require explicit owner approval.
9. Never put credentials, unpublished private documents, private student records, grant files, or private original-asset backups into this public repository. Record asset provenance and unknown permission status in `ASSET_SOURCES.md` without guessing.
10. Maintain `CHANGELOG.md`, release tags, and the backup instructions. Keep the approved Version 6 rollback. Never force-push or replace an existing GitHub repository during setup without inspecting and preserving its current work.
11. Verify actual GitHub deployment status and public HTTPS responses before calling the migration live. Do not describe source-based checks or simulated interaction checks as browser/device testing. Record genuine test limitations.
