# Dependencies and cost controls

| Dependency | Purpose | Cost / maintenance note |
| --- | --- | --- |
| Static HTML/CSS/JavaScript | Complete visitor-facing site | No framework, server, database, or runtime subscription |
| Python 3.10+ standard library | Generate HTML and verify content/links | No Python packages need installation |
| Node.js 18+ | Development syntax and simulated interaction checks | No npm packages; not required for visitors |
| DM Sans and Manrope via Google Fonts | Existing approved typography | Existing stylesheet import in `dist/style.css`; external font requests remain exactly as approved; system fallbacks are already defined |
| Official GitHub Actions | Checkout, build, artifact, Pages deployment | Standard Ubuntu runners; no larger runners, caches, custom images, paid actions, or custom secrets |
| GitHub Pages | Public static hosting | Public repository on GitHub Free; standard Pages use is free within published service limits |
| Optional domain registrar | `solankilab.org` only if owner approves | Separate domain registration/renewal expense; no purchase or registrar account is configured by this package |

No analytics, trackers, remote image-generation API, external image CDN, or runtime API calls are added. Existing links to collaborators and institutions remain ordinary hyperlinks, not runtime data dependencies.

The workflow uploads only the roughly 19 MB public site as a Pages artifact, retains it for one day, and creates no additional build artifacts or caches. Do not increase a GitHub spending budget, switch to a paid runner, activate a paid plan/trial, or add a billed service without explicit owner approval. Keep account spending limits at $0 where applicable.

Official references checked during launch preparation:

- [GitHub Pages availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [DM Sans source family](https://fonts.google.com/specimen/DM+Sans)
- [Manrope source family](https://fonts.google.com/specimen/Manrope)
