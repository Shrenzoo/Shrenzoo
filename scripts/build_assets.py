"""Regenerate the profile's original SVG artwork using Python's standard library."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
BG, PANEL, INK, MUTED, MINT, AMBER = (
    "#101a20", "#17262e", "#f2f6f4", "#acbec5", "#8fe3c3", "#ffbb7d"
)


def svg(name, width, height, content, description):
    source = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(name.replace('-', ' ').title())}</title>
<desc id="desc">{escape(description)}</desc>
<style>text{{font-family:Arial,Helvetica,sans-serif}}.mono{{font-family:Consolas,Menlo,monospace}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<rect width="{width}" height="{height}" rx="18" fill="{BG}"/>
{content}
</svg>'''
    (ASSETS / f"{name}.svg").write_text(source)
    poster = re.sub(r"<animate(?:Transform|Motion)?\b[^>]*(?:/>|>.*?</animate(?:Transform|Motion)?>)", "", source, flags=re.S)
    (ASSETS / f"{name}-static.svg").write_text(poster)


def text(x, y, content, size=20, color=INK, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(content)}</text>'


def pulse():
    return '<animate attributeName="opacity" values="1;0.35;1" dur="4s" repeatCount="indefinite"/>'


hero = f'''<defs>
  <radialGradient id="halo"><stop stop-color="{MINT}" stop-opacity=".16"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#31464f"/></pattern>
</defs>
<rect x="590" y="1" width="369" height="358" fill="url(#dots)"/>
<circle cx="759" cy="175" r="180" fill="url(#halo)"/>
{text(44, 49, 'shrenzoo / build log', 16, MUTED, 'class="mono"')}
{text(42, 128, 'Shreyas', 65, INK, 'font-weight="700" letter-spacing="-3"')}
{text(42, 201, 'Pabbathi.', 65, INK, 'font-weight="700" letter-spacing="-3"')}
{text(46, 253, 'Ideas into things you can use.', 25, MINT)}
{text(46, 315, 'AI tools  /  creative systems  /  open source', 16, MUTED, 'class="mono"')}
<g transform="translate(757 172)" fill="none" stroke="{MINT}">
  <circle r="104" stroke-opacity=".24"/>
  <circle r="72" stroke-opacity=".2"/>
  <ellipse rx="120" ry="43" transform="rotate(-36)" stroke-opacity=".6"/>
  <ellipse rx="120" ry="43" transform="rotate(36)" stroke-opacity=".35"/>
  <g stroke-width="1.5">
    <path d="M0 -67 59 -34 59 34 0 68 -59 34 -59 -34Z M0 0 0 68 M0 0 59 -34 M0 0 -59 -34 M0 -67 0 0"/>
    <path d="M-59 34 0 0 59 34" stroke-dasharray="3 5" stroke-opacity=".35"/>
    <animateTransform attributeName="transform" type="rotate" values="0;360" dur="32s" repeatCount="indefinite"/>
  </g>
  <g><circle cx="104" r="6" fill="{AMBER}" stroke="{BG}" stroke-width="4"/>
    <animateTransform attributeName="transform" type="rotate" values="0;360" dur="16s" repeatCount="indefinite"/>
  </g>
  <g><circle cx="-72" r="4" fill="{MINT}" stroke="none"/>
    <animateTransform attributeName="transform" type="rotate" values="0;-360" dur="22s" repeatCount="indefinite"/>
  </g>
</g>
<path d="M650 307H893" stroke="#31464f"/>
{text(651, 332, 'think / build / refine', 15, MUTED, 'class="mono"')}
'''
svg("hero", 960, 360, hero, "Shreyas Pabbathi. Ideas into things you can use. AI tools, creative systems, and open source. A wireframe cube rotates inside orbital rings.")

steps = len("Build it. Try it. Make it better.")
typing_values = ";".join([str(i * 15) for i in range(steps + 1)] + [str(steps * 15), "0"])
typing_times = ";".join([f"{i * .48 / steps:.5f}" for i in range(steps + 1)] + ["0.94", "1"])
terminal = f'''<defs><clipPath id="typing"><rect x="54" y="149" width="850" height="40"><animate attributeName="width" values="{typing_values}" keyTimes="{typing_times}" dur="12s" repeatCount="indefinite" calcMode="discrete"/></rect></clipPath></defs>
<path d="M0 52H960" stroke="#31464f"/>
<circle cx="29" cy="26" r="5" fill="{AMBER}"/>
<circle cx="49" cy="26" r="5" fill="{MINT}"/>
<circle cx="69" cy="26" r="5" fill="#617c88"/>
{text(101, 33, 'shrenzoo / workshop', 17, MUTED, 'class="mono"')}
{text(28, 105, '$ cat focus.txt', 25, MINT, 'class="mono"')}
{text(28, 145, 'AI that helps. Interfaces that make sense.', 25, INK, 'class="mono"')}
<g clip-path="url(#typing)">{text(54, 181, 'Build it. Try it. Make it better.', 25, AMBER, 'class="mono"')}</g>
<rect x="29" y="161" width="12" height="24" fill="{MINT}">{pulse()}</rect>
'''
svg("workshop", 960, 214, terminal, "Workshop terminal: AI that helps. Interfaces that make sense. Build it. Try it. Make it better.")

art = {
    "unlock": f'''<g transform="translate(340 78)" fill="none" stroke="{MINT}" stroke-width="1.6">
      <path d="M-48 10 0 -16 48 10 0 36Z M-48 10V38L0 65 48 38V10 M0 36V65"/>
      <g><path d="M-33 -31 0 -50 33 -31 0 -12Z M-33 -31V-11L0 8 33 -11V-31 M0 -12V8" fill="{PANEL}"/>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -14;0 0" dur="5s" repeatCount="indefinite"/></g>
      <path d="M-55 49 -72 59 M55 49 72 59" stroke="{AMBER}"/>
    </g>''',
    "diverge": f'''<g fill="none" stroke="{MINT}" stroke-width="2">
      <path d="M276 89H300Q316 89 329 70T376 49 M300 89Q316 89 329 108T376 131 M300 89H376" stroke-opacity=".45"/>
      <circle cx="279" cy="89" r="6" fill="{MINT}"/>
      <g fill="{BG}"><circle cx="377" cy="49" r="8"/><circle cx="377" cy="89" r="8"/><circle cx="377" cy="131" r="8"/></g>
      <circle r="4" fill="{AMBER}" stroke="none"><animateMotion path="M279 89H300Q316 89 329 70T376 49" dur="4s" repeatCount="indefinite"/></circle>
    </g>''',
    "incident-bridge": f'''<g fill="none" stroke="{MINT}" stroke-width="2">
      <circle cx="282" cy="89" r="19"/><circle cx="382" cy="89" r="19"/>
      <path d="M303 89H361" stroke-dasharray="3 6" stroke-opacity=".5"/>
      <circle r="5" fill="{AMBER}" stroke="none"><animateMotion path="M305 89H359" dur="3s" repeatCount="indefinite"/></circle>
      <path d="M275 89 280 94 290 83 M375 89 380 94 390 83"/>
    </g>''',
    "goldpal": f'''<g transform="translate(330 88)">
      <circle r="53" fill="{AMBER}" fill-opacity=".08"/>
      <path d="M-29 -27H29V14H3L-13 28V14H-29Z" fill="none" stroke="{AMBER}" stroke-width="2"/>
      <g fill="{AMBER}"><circle cx="-13" cy="-7" r="3"/>
      <circle cy="-7" r="3">{pulse()}</circle><circle cx="13" cy="-7" r="3"/></g>
    </g>''',
}
for key, title, category in [
    ("unlock", "UNLOCK", "AI + mechanical repair"),
    ("diverge", "Diverge", "Creative reasoning"),
    ("incident-bridge", "IncidentBridge", "Agent collaboration"),
    ("goldpal", "GoldPal", "Accessible iOS"),
]:
    content = text(25, 45, category, 15, MUTED)
    content += text(25, 99, title, 29, INK, 'font-weight="700" letter-spacing="-1"')
    content += text(25, 143, 'Explore the project', 14, MINT)
    content += art[key]
    svg(key, 440, 178, content, f"{title}: {category}. Explore the project.")

print(f"Generated {len(list(ASSETS.glob('*.svg')))} SVG files.")
