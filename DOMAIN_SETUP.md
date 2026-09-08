# Optional custom domain

Preferred domain: **solankilab.org**. Its availability, ownership, and registrar price have not been confirmed, and no purchase is authorized or made. The initial GitHub Pages launch does not require a domain purchase.

Keep the free GitHub Pages URL in `site-config.json` until the owner confirms domain ownership or approves a specific registrar price. Do not create a premature CNAME configuration or direct an unowned domain at the site.

When the owner is ready, the maintainer should check current domain availability, confirm the exact initial and renewal price, and obtain approval before any purchase. The domain/registrar account must remain under the owner's control. Hosting should remain free.

For a domain the owner controls:

1. Verify ownership in GitHub, using the TXT record GitHub supplies for this account.
2. Add the approved apex domain in the repository's Pages settings before pointing DNS at GitHub Pages.
3. Use the DNS values in GitHub's current official instructions. For the `www` subdomain, the CNAME target is the owner's `shysol4u.github.io` host, with no repository path.
4. Select the apex domain as canonical; configure both apex and `www` so GitHub can redirect to the preferred address.
5. Enable HTTPS once GitHub reports the certificate is ready. Verify both names, redirects, every page, and the source/code/image assets.
6. Set `site_url` to `https://solankilab.org`, rebuild, check, and publish so canonical URLs and the sitemap match.

The current custom Actions workflow does not require a CNAME file in the uploaded site; the repository's Pages settings hold the domain configuration. Recheck current GitHub guidance during setup rather than copying stale DNS instructions.

[Official custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
