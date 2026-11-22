"""Create static alternatives to the generated contribution animations."""

from pathlib import Path
import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")
root = Path(__file__).resolve().parents[1]
for name in ("contributions", "contributions-dark"):
    source = root / "assets" / f"{name}.svg"
    tree = ET.parse(source)
    svg = tree.getroot()
    style = ET.SubElement(svg, "{http://www.w3.org/2000/svg}style")
    style.text = "* { animation: none !important; transition: none !important; }"
    tree.write(source.with_stem(f"{name}-static"), encoding="unicode")
