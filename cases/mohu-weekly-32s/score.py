#!/usr/bin/env python3
"""score.py — the film's sound, placed from comp.html's window.__events(). Synthesised palette only, one room.
Struck-glass tones are tuned to a Hijaz scale on D (D Eb F# G A Bb C) for the Islamic register.
  python3 score.py   → sfx.wav"""
import asyncio, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from sfx_palette import *
from playwright.async_api import async_playwright

async def events():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "comp.html"))); await pg.evaluate("window.__ready")
        e = await pg.evaluate("window.__events()"); await b.close(); return e

HZ = [293.66, 311.13, 369.99, 392.0, 440.0, 466.16, 523.25, 587.33, 622.25, 739.99, 783.99, 880.0]   # D hijaz, two octaves
def main():
    E = asyncio.run(events()); s = Score(dur=34, T60=2.2)
    s.place(sub(40, 3.5) * 0.6, 0.0, 0.25, send=0.6)                         # a low bed under the opening
    for ev in E:
        k, t = ev[0], ev[1]; i = ev[2] if len(ev) > 2 else 0
        if k == 'seed': s.place(glass(HZ[7], 1.6, 0.5), t, 0.22, send=0.7)
        elif k in ('drawA', 'drawB'): s.place(air(1.2, 180, 1400, 1.2, 0.6), t, 0.32, pan=-0.3 if k == 'drawA' else 0.3, send=0.6)
        elif k == 'land': s.place(sub(55, 1.4), t, 0.55, send=0.5); s.place(glass(HZ[0], 2.4, 0.6), t, 0.22, send=0.8); s.place(glass(HZ[4], 2.2, 0.4), t + 0.02, 0.12, send=0.8)
        elif k in ('words', 'date', 'org'): s.place(wood(220, 0.08), t, 0.16, send=0.3)
        elif k == 'lift': s.place(air(0.9, 300, 3200, 1.3, 0.5), t, 0.5, send=0.5)
        elif k == 'iris': s.place(sub(48, 1.0), t + 0.3, 0.35, send=0.5)
        elif k == 'tabs': s.place(wood(260, 0.07), t, 0.18); s.place(wood(300, 0.07), t + 0.1, 0.14)
        elif k == 'count': s.place(glass(HZ[7], 1.4, 0.7), t, 0.24, send=0.6); s.place(sub(62, 0.6), t, 0.3)
        elif k == 'cell': s.place(bubble(420 + 60 * i, 0.2), t, 0.16, pan=0.3 - 0.2 * i, send=0.3)
        elif k == 'bar': s.place(wood(170 + 18 * i, 0.07), t, 0.14, pan=0.2, send=0.25)
        elif k == 'pill': s.place(air(0.45, 400, 2600, 1.6, 0.4), t, 0.4, pan=0.4, pan_to=-0.3, send=0.4)
        elif k == 'roll':
            n = [None, HZ[3], HZ[4], HZ[2]][i]; s.place(glass(n * 2, 1.5, 0.7), t, 0.24, send=0.6); s.place(sub(58 if i != 2 else 46, 0.8), t, 0.38 if i == 2 else 0.26)
        elif k == 'reflow': s.place(air(0.8, 220, 1500, 1.0, 0.5), t, 0.22, send=0.4)
        elif k == 'ring': s.place(glass([HZ[7], HZ[8], HZ[9], HZ[11]][i], 1.6, 0.5), t, 0.18, pan=-0.2 + 0.15 * i, send=0.7)
        elif k == 'out': s.place(air(1.0, 2600, 260, 1.2, 0.5), t, 0.42, send=0.5)
        elif k == 'close': s.place(sub(44, 2.0), t, 0.5, send=0.6); s.place(glass(HZ[0], 3.0, 0.5), t, 0.2, send=0.9); s.place(glass(HZ[7], 3.0, 0.4), t + 0.03, 0.12, send=0.9)
        elif k in ('thanks', 'org2'): s.place(wood(200, 0.09), t, 0.14, send=0.4)
    s.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx.wav"), peak_db=-6.0)
main()
