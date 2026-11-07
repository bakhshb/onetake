#!/usr/bin/env python3
"""score.py — sound only at the scene transitions, placed from comp.html's window.__events(). Synthesised palette,
one room; swipes only.   python3 score.py → sfx.wav"""
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
    for k, t, i in E:          # a swipe (air) at each transition — no bells, no thuds
        if k == 'open': s.place(air(1.1, 220, 2600, 1.2, 0.5), t - 0.3, 0.45, pan=-0.2, pan_to=0.2, send=0.45)
        elif k == 'move':
            p = 0.35 if i % 2 else -0.35
            s.place(air(0.8, 260, 2800, 1.4, 0.5), t, 0.42, pan=p, pan_to=-p, send=0.4)
        elif k == 'close': s.place(air(1.1, 2600, 240, 1.2, 0.5), t - 0.35, 0.45, pan=0.2, pan_to=-0.2, send=0.45)
    s.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sfx.wav"), peak_db=-6.0)
main()
