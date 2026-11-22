# Maintaining this profile

`README.md` on this repository's default branch appears on [Shreyas's GitHub profile](https://github.com/Shrenzoo).

## Content

- Lead with UNLOCK and Diverge, whose demos, source, and evidence a visitor can inspect.
- Describe what each project does in plain language, then link the repository or demo that shows it.
- The [UNLOCK CAD animation](https://github.com/Shrenzoo/unlock/tree/main/assets/readme) depicts the synthetic B05 battery fixture and a 12 mm strap move.
- A geometric pass establishes a checked removal route under fixture constraints; it does not establish strength or physical safety.
- The [Diverge README](https://github.com/Shrenzoo/diverge) supplies the grade-dashboard illustration; it is not an observed test result.
- The [Diverge pilot](https://github.com/Shrenzoo/diverge/blob/main/evals/pilot/README.md) records artifacts, scores, and limitations; link there for evaluation claims.
- Keep [IncidentBridge](https://github.com/Shrenzoo/incident_bridge) labeled a hackathon prototype and [GoldPal](https://github.com/Shrenzoo/GoldPal) an iOS project.
- Open each demo, source, example, and evidence link after changing it; the label should match its destination.

## Media and motion

- GitHub renders and sanitizes the README; use supported Markdown and HTML for layout and motion choices.
- The UNLOCK GIF and poster files live in [`unlock/assets/readme`](https://github.com/Shrenzoo/unlock/tree/e57594c713ea4970b399c01c22192290f267dcd3/assets/readme).
- README media URLs pin UNLOCK commit `e57594c713ea4970b399c01c22192290f267dcd3`; check all four media paths before changing it.
- Update light and dark variants together; review each against GitHub's matching theme.
- Each animated `<picture>` has a still source for `prefers-reduced-motion: reduce`; retain that source when replacing media.
- `scripts/build_assets.py` builds `decision-light.svg`, `decision-dark.svg`, and both `-static.svg` variants with Python's standard library.
- Rebuild the decision sketches with `python3 scripts/build_assets.py` after editing the generator.
- `.github/workflows/contributions.yml` refreshes the contribution snake at 08:17 UTC daily and allows manual dispatch.
- `scripts/snake_posters.py` makes light and dark snake posters by adding a CSS rule that disables animation and transitions.
- The snake workflow stages `assets/contributions*.svg` and commits only when that artwork changes.
- Credit Platane/snk for the snake and the UNLOCK creators for the CAD animation.

## Publishing

- The profile repository matches the username `Shrenzoo`; publishing `README.md` and assets on `main` updates the profile.
- GitHub attributes commits by account identity; check the published commit's author when contribution counting matters.
- When changing the pinned UNLOCK commit, verify the referenced GIF and poster paths in that exact commit.
- Give each image alt text that explains the meaningful result without requiring motion.
- Keep synthetic-research and evaluation limits near the claims they qualify.

## Quick checks

- Run `python3 scripts/build_assets.py` before reviewing a decision-sketch change.
- Parse each generated SVG as XML and inspect both color schemes.
- Check decision-sketch stills for absent `animateMotion`; check snake posters for their animation-disabling CSS rule.
- Review the profile on GitHub after publishing; README rendering can differ from local previews.
