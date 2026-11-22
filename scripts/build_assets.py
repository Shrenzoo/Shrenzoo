"""Build the profile's Diverge decision sketch without external dependencies.

Design process: unslop by Damir Sokolovsky, https://heydamir.design/unslop,
licensed CC BY 4.0. The diagram illustrates the dashboard example in Diverge.
"""

from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)

for theme, background, ink, muted, line, accent in (
    ("dark", "#0d1117", "#f0f6fc", "#9198a1", "#59636e", "#79b8ff"),
    ("light", "#ffffff", "#1f2328", "#59636e", "#9198a1", "#0969da"),
):
    for static in (False, True):
        motion = "" if static else f'''<circle r="4" fill="{accent}">
  <animateMotion path="M188 100 H232 Q252 100 252 120 V152 H324" dur="8s" keyPoints="0;1;1" keyTimes="0;0.45;1" calcMode="linear" repeatCount="indefinite"/>
</circle>'''
        source = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 600 200" role="img" aria-labelledby="title desc">
<title id="title">One brief, two useful directions</title>
<desc id="desc">Diverge's illustrative grade-dashboard example: add more charts, or help a student forecast the score they need. The forecast is the selected direction.</desc>
<rect width="600" height="200" fill="{background}"/>
<g fill="none" stroke="{line}" stroke-width="1.5" stroke-linejoin="round">
  <rect x="12" y="64" width="176" height="72" rx="8"/>
  <path d="M188 100 H232 Q252 100 252 80 V44 H324"/>
  <path d="M188 100 H232 Q252 100 252 120 V152 H324" stroke="{accent}"/>
  <rect x="324" y="12" width="264" height="64" rx="8"/>
  <rect x="324" y="120" width="264" height="64" rx="8" stroke="{accent}"/>
</g>
<g font-family="Arial,Helvetica,sans-serif" font-size="22" fill="{ink}">
  <text x="100" y="93" text-anchor="middle">Grade</text>
  <text x="100" y="120" text-anchor="middle">dashboard</text>
  <text x="348" y="52" fill="{muted}">More charts</text>
  <text x="348" y="160">Forecast a score</text>
</g>
<path d="M550 151 l6 6 12 -14" fill="none" stroke="{accent}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
{motion}
</svg>
'''
        suffix = "-static" if static else ""
        (ASSETS / f"decision-{theme}{suffix}.svg").write_text(source)

print("Built four decision sketches: light, dark, and static alternatives.")
