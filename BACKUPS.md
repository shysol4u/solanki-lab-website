# Backups and recovery

The project is protected by three separate layers:

1. **GitHub history after initial upload:** `main` is the production source; `approved-v6` preserves the imported approved design; `v6.0.0` preserves the initial technical launch package; `v6.0.1` preserves the verified custom-domain website. Tag future approved major updates without moving existing tags.
2. **Downloadable source ZIP:** `SolankiLab_Website_v6_GitHub.zip` contains the complete editable launch repository and workflow, excluding Git credentials and private master backups.
3. **Separate private backup:** `SolankiLab_Private_Backup_v6.zip` contains original supplied documents/assets, an original-history Git bundle with Versions 1–6, and a Git bundle for the prepared GitHub launch repository. Keep this archive private; it is not a public GitHub release asset.

The original media are preserved at the best resolution actually supplied. A higher-resolution camera original or vector logo is not invented where none was provided. Original orientation and bytes are kept privately; the website retains its approved web versions.

Backup limitation: the current local copy of the first `WEBSITE_UPDATED.docx` is incomplete. Its complete earlier extracted text, rendered PDF, extraction map, and all 26 original embedded media are retained instead, along with the partial container for diagnosis. The later source documents and complete editable Version 6 website are intact. No missing source document has been fabricated.

## Confirmed public rollback identities

- `approved-v6`: `e41091e276009d656c0e5a8cb68e900ad5e576ec`; also retained on `rollback/approved-v6`.
- `v6.0.0`: `6ecab33eeebb178cd31f1535d13405381bbac984`.
- `v6.0.1`: `2588a38a8ee313079888d9a09c02a94d1a9ee03a`; verified website at `https://solankilab.org/`.

The imported GitHub commits have new IDs but exactly the same complete file trees as the original two launch commits. `audit/launch-provenance.json` records the mapping. The private bundles preserve the original commit objects and all earlier Versions 1–6; do not move existing tags or publish those private archives.

## Restore a normal future update

Inspect GitHub history, identify the last working change, and use a revert commit on `main` when appropriate. Rebuild/check and let the standard workflow redeploy. Do not force-push away history or blindly patch production.

## Domain configuration recovery

Domain configuration is separate from Git history. Reverting a source commit does not undo Porkbun DNS or GitHub Pages settings. For a source rollback, retain the current working domain metadata unless the domain change itself is being reverted. Keep GitHub's ownership TXT record in DNS. The original Porkbun parking defaults were an apex `ALIAS` and wildcard `CNAME`, both pointing to `pixie.porkbun.com` with TTL 600; these are recorded only for recovery context and are not the production website configuration.

## Recover the original pre-migration history

Extract the private backup and use its original-history bundle in a **private** working directory:

```bash
git clone history/solanki-original-versions-1-to-6.bundle recovered-solanki-history
```

The original approved tags are `user-version-1` through `user-version-6`. That repository includes private source instructions/master documents and must not be pushed wholesale to a public repository.

## Recover this GitHub launch repository

```bash
git clone history/solanki-github-launch-v6.bundle recovered-solanki-launch
```

The source ZIP can also reconstruct the project without Git history. Follow the README build instructions; source assets in `dist/` must remain present.

## Make a later portable backup

From a clean, committed repository:

```bash
git archive --format=zip --prefix=solanki-lab-website/ --output=../SolankiLab_Website_backup.zip HEAD
git bundle create ../SolankiLab_Website_history.bundle --all
```

Store copies under the owner's control. Keep originals and confidential source material separate from the public website repository. Never put authentication tokens, private keys, or local credential configuration in a backup intended for sharing.
