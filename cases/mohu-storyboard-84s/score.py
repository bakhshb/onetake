#!/usr/bin/env python3
"""score.py — sound only at the scene transitions, placed from comp.html's window.__events(). Synthesised palette,
one room; struck-glass landings tuned to a Hijaz scale on D.   python3 score.py → sfx.wav"""
import asyncio, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts"))
from sfx_palette import *
from playwright.async_api import async_playwright

async def events():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto("file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "comp.html"))); await pg.evaluate("window.__ready")
        e = await pg.evaluate("window.__events()"); await b.close(); return e

HZ = [293.66, 311.13, 369.99, 392.0, 440.0, 466.16, 523.25, 587.33, 622.25, 739.99, 783.99, 880.0]
def main():
    E = asyncio.run(events()); s = Score(dur=84, T60=2.0)
    for k, t, i in E:
        if k == 'open':
            s.place(air(1.0, 200, 2400, 1.2, 0.55), t - 0.35, 0.42, send=0.5); s.place(sub(48, 1.4), t + 0.35, 0.4, send=0.5)
            s.place(glass(HZ[7], 2.2, 0.55), t + 0.6, 0.2, send=0.8); s.place(glass(HZ[4], 2.0, 0.4), t + 0.62, 0.1, send=0.8)
        elif k == 'move':
            p = 0.35 if i % 2 else -0.35
            s.place(air(0.75, 260, 2800, 1.4, 0.5), t, 0.34, pan=p, pan_to=-p, send=0.45)
            s.place(glass(HZ[[0, 7, 4, 9, 3, 8, 2, 7, 4, 0][i]] * (1 if i % 3 else 2), 1.6, 0.6), t + 0.85, 0.15, send=0.7)
            s.place(sub(58, 0.6), t + 0.85, 0.16)
        elif k == 'close':
            s.place(air(1.1, 2600, 240, 1.2, 0.5), t - 0.4, 0.4, send=0.5); s.place(sub(44, 2.2), t + 0.6, 0.5, send=0.6)
            s.place(glass(HZ[0], 3.2, 0.5), t + 0.6, 0.2, send=0.9); s.place(glass(HZ[7], 3.2, 0.4), t + 0.63, 0.12, send=0.9)
    s.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx.wav"), peak_db=-6.0)
main()
