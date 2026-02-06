
# Contributing to Noetivis

## Principles
Noetivis is a platform economy. Contributions are welcomed and credited.

## How to contribute
1) Fork the repo
2) Create a branch: feature/<name>
3) Open a PR with:
   - clear description
   - tests or reproduction steps
   - screenshots if UI changes

## Commission-aware contributions (Ecosystem rules)
- The platform includes a commission model (founder + contributors + partners/resellers + owners).
- Code contributions can qualify for contributor allocation weight in the contributors pool.
- Maintainers may assign or adjust allocation weights based on:
  - impact
  - complexity
  - maintenance burden
  - security responsibility

## Contributor allocation process (MVP policy)
- Each accepted PR can add points.
- Quarterly: points are translated into weights in `contributor_allocations`.
- Distribution is executed via `/distribute/contributors`.

## Code standards
- Keep endpoints auditable.
- Keep data access consent-first and authorized.
- Avoid collecting private data without explicit user authorization.

## License
By contributing, you agree your contributions are licensed under the repo license.
