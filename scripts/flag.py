"""Escribe assets/flag.svg (Union Jack simplificada) y assets/favicon.svg."""

from pathlib import Path

NAVY = "#012169"
RED = "#C8102E"
WHITE = "#FFFFFF"

# Bandera 60x30: diagonales blancas y rojas (las rojas, recortadas) y cruz de San Jorge sobre cruz blanca.
flag = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 30">'
    '<clipPath id="s"><path d="M0,0 v30 h60 v-30 z"/></clipPath>'
    '<clipPath id="t"><path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z"/></clipPath>'
    '<g clip-path="url(#s)">'
    f'<path d="M0,0 v30 h60 v-30 z" fill="{NAVY}"/>'
    f'<path d="M0,0 L60,30 M60,0 L0,30" stroke="{WHITE}" stroke-width="6"/>'
    f'<path d="M0,0 L60,30 M60,0 L0,30" clip-path="url(#t)" stroke="{RED}" stroke-width="4"/>'
    f'<path d="M30,0 v30 M0,15 h60" stroke="{WHITE}" stroke-width="10"/>'
    f'<path d="M30,0 v30 M0,15 h60" stroke="{RED}" stroke-width="6"/>'
    "</g>"
    "</svg>"
)

# Favicon 64x64 con esquinas redondeadas y la misma composición simplificada.
favicon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<clipPath id="r"><rect width="64" height="64" rx="14"/></clipPath>'
    '<g clip-path="url(#r)">'
    f'<rect width="64" height="64" fill="{NAVY}"/>'
    f'<path d="M0,0 L64,64 M64,0 L0,64" stroke="{WHITE}" stroke-width="12"/>'
    f'<path d="M0,0 L64,64 M64,0 L0,64" stroke="{RED}" stroke-width="5"/>'
    f'<path d="M32,0 V64 M0,32 H64" stroke="{WHITE}" stroke-width="20"/>'
    f'<path d="M32,0 V64 M0,32 H64" stroke="{RED}" stroke-width="12"/>'
    "</g>"
    "</svg>"
)

assets = Path(__file__).resolve().parents[1] / "assets"
assets.joinpath("flag.svg").write_text(flag, encoding="utf-8")
assets.joinpath("favicon.svg").write_text(favicon, encoding="utf-8")
