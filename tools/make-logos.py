# -*- coding: utf-8 -*-
"""Generates the three generic payment icons that have no official brand artwork.

Everything else in images/logos/ is the brand's real logo — see images/logos/SOURCES.md.

    python tools/make-logos.py
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "images", "logos")
os.makedirs(OUT, exist_ok=True)

AR = "Tahoma, 'Segoe UI', Arial, sans-serif"   # single quotes: this sits inside an XML attribute
SA = "Arial, Helvetica, sans-serif"


def write(name, label, body):
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 80" width="240" height="80" '
                f'role="img" aria-label="{label}">{body}\n</svg>\n')


write("cash", "كاش Cash", f'''
<g fill="none" stroke="#1E7A4B" stroke-width="4" stroke-linejoin="round">
  <path d="M24 18h56a8 8 0 0 1 8 8v28" stroke-opacity=".4"/>
  <rect x="14" y="26" width="62" height="36" rx="6"/>
  <circle cx="45" cy="44" r="9"/>
</g>
<text x="102" y="52" font-family="{SA}" font-size="30" font-weight="bold"
      fill="#1E7A4B" letter-spacing="2">CASH</text>''')

write("wallet", "محفظة إلكترونية E-wallet", f'''
<g fill="none" stroke="#B4471C" stroke-width="4.5" stroke-linejoin="round" stroke-linecap="round">
  <path d="M74 28H26a10 10 0 0 0-10 10v18a10 10 0 0 0 10 10h48a6 6 0 0 0 6-6V34a6 6 0 0 0-6-6Z"/>
  <path d="M16 38V28a8 8 0 0 1 5.6-7.6l38-11"/>
</g>
<circle cx="66" cy="47" r="5.5" fill="#B4471C"/>
<text x="96" y="40" font-family="{AR}" font-size="22" font-weight="bold" fill="#2A1D16">محفظة</text>
<text x="96" y="62" font-family="{SA}" font-size="14" fill="#6B5646" letter-spacing="1.5">E-WALLET</text>''')

write("all-banks", "كل البنوك All banks", f'''
<g fill="none" stroke="#2A1D16" stroke-width="4" stroke-linejoin="round">
  <rect x="14" y="20" width="66" height="44" rx="7"/><path d="M14 34h66"/>
</g>
<rect x="22" y="45" width="22" height="7" rx="3.5" fill="#2A1D16"/>
<text x="94" y="40" font-family="{AR}" font-size="22" font-weight="bold" fill="#2A1D16">كل البنوك</text>
<text x="94" y="63" font-family="{SA}" font-size="15" fill="#6B5646" letter-spacing="2">ALL BANKS</text>''')

print("wrote 3 generic icons")
