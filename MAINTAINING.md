# Maintaining this profile

`README.md` on this repository's default branch appears on [Shreyas's GitHub profile](https://github.com/Shrenzoo).

## Content

- Lead with UNLOCK and Diverge, whose demos, source, and evidence a visitor can inspect.
- Describe what each project does in plain language, then link the repository or demo that shows it.
- The [UNLOCK CAD animation](https://github.com/Shrenzoo/unlock/tree/main/assets/readme) depicts the synthetic B05 battery fixture and a 12 mm strap move.
- Describe geometric checks as geometric checks; they do not establish strength or physical safety.
- Diverge's grade-dashboard branch is an illustration from its README, not an observed test result.
- The Diverge pilot has its own artifacts, scores, and limitations; link directly to them when mentioning it.
- Keep IncidentBridge labeled as a hackathon prototype and GoldPal as an iOS project.
- Check that demo, source, example, and evidence links point to the specific promised destination.

## Media and motion

- GitHub renders this profile as a README; use supported Markdown and HTML rather than page scripts.
- The UNLOCK GIF and poster files live in `Shrenzoo/unlock/assets/readme/`.
- README media URLs pin a UNLOCK commit so later upstream changes cannot silently alter this page.
- Keep light and dark variants paired when changing a visual.
- Keep a still poster for every animated visual under `prefers-reduced-motion: reduce`.
- `scripts/build_assets.py` generates the four Diverge decision sketches with Python's standard library.
- Rebuild the decision sketches with `python3 scripts/build_assets.py` after editing the generator.
- `.github/workflows/contributions.yml` refreshes the contribution snake daily.
- `scripts/snake_posters.py` creates static alternatives for the snake's light and dark versions.
- The snake workflow writes only contribution assets when their contents change.
- Credit Platane/snk for the snake and the UNLOCK creators for the CAD animation.

## Publishing

- The default branch is `main`; publish README and asset changes there to update the profile.
- GitHub attributes commits by account identity; check the published commit's author when contribution counting matters.
- When changing the pinned UNLOCK commit, verify the referenced GIF and poster paths in that exact commit.
- Give each image alt text that explains the meaningful result without requiring motion.
- Keep synthetic-research and evaluation limits near the claims they qualify.

## Quick checks

- Run `python3 scripts/build_assets.py` before reviewing a decision-sketch change.
- Parse each generated SVG as XML and inspect both color schemes.
- Check that the static variants contain no SVG animation elements.
- Review the profile on GitHub after publishing; README rendering can differ from local previews.
