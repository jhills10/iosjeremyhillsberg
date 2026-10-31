# Publication Policy

## Allowed source material

Original educational writing, independently created examples using synthetic data, and citations to public documentation are welcome. Keep a source list in each technical resource so a reviewer can assess its provenance.

## Prohibited material

Never import Grid Health source code, secrets, customer data, or private business information. This includes internal architecture, business plans, private URLs, support records, screenshots, logs, database exports, and content derived from private repositories. Redacting names or rewriting an excerpt does not make it eligible for publication.

Do not commit credentials, signing material, provisioning profiles, environment files, device backups, build output, or real user data. Use obvious placeholders in examples.

## Before publication

1. Confirm every added file has an acceptable origin. Review images, attachments, and generated content as carefully as prose.
2. Inspect the complete diff and untracked files. Confirm examples are independently written and synthetic.
3. Run `python3 scripts/check_publication.py`. Resolve findings without bypassing the check.
4. Confirm source links and technical claims. Disclose validation limits.
5. Have a maintainer review the pull request checklist before merging.

## Repository settings to enable

These are maintainer setup recommendations, not settings applied by this repository:

- Protect `main` with pull requests and require the `publication-check` status check.
- Require an independent approval when another reviewer is available, and dismiss stale approvals after changes.
- Enable GitHub secret scanning and push protection where available.
- Restrict bypass rights and use least-privilege workflow permissions.

## Limits and incident handling

The local check scans tracked and non-ignored untracked working-tree files. It does not audit Git history, ignored files, remote settings, or every possible secret format. It cannot establish originality or detect all private business information. Ignore rules are convenience controls, not access controls.

If sensitive material is found, stop publication and avoid repeating its contents in issues or chat. Notify the repository owner privately. Revoke exposed credentials at their issuer and coordinate removal from history and downstream copies where needed. Deleting the latest file alone does not remove earlier published versions.
