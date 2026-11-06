# mohu-weekly — تقرير الإنجاز الأسبوعي · 34 s, vertical 1080×1920

A one-take motion summary of the Ministry of Hajj & Umrah weekly achievement report (5 November 2026):
strategic tasks, Suhail projects, transactions and digital-experience maturity. Data, section order and colours
are taken from the report PDF.

**Concept — one star carries the whole film.** The eight-pointed star (khatam / rub' el hizb) that numbers the
report's pages is the subject. It is drawn in gold on Kiswa black, opens the report's cream page with an iris,
holds each section's total in its centre, turns one point (45°) at every section, and finally becomes the hub of a
rosette whose four rings are the four maturity dimensions. At the end the cream page closes back into it on black.
A girih lattice of the same star sits farther back on both grounds, so every camera move has something to slide
against.

## Beat sheet

| t (s) | beat | what moves | what carries into the next beat |
|---|---|---|---|
| 0–2.6 | a gold point, two squares drawn stroke by stroke | the camera pulls out 1.8× → 1×, the lattice is revealed from the star outward | the star |
| 2.6–5.6 | title, date, ministry · **hold** | words rise, then nothing | the star |
| 5.6–6.9 | title lifts away, the star arcs to the hero card and an iris opens the cream page from it | star, iris | the star becomes the total's medallion |
| 6.9–8.8 | tabs, KPI card, 22 counts up in the star, four status numbers hop out of it, sector bars grow | camera follows the star, then pulls back | tab pill, star, bars |
| 8.8–11.6 | **hold** — tasks | — | |
| 11.6–13.8 | Suhail: the pill stretches to the next tab and changes colour, the star turns one point and rolls 22 → 19, cells roll, rows re-sort by sector | whip to the hero, pull back | the same pill, star, rows |
| 13.8–16.4 | **hold** — Suhail | — | |
| 16.4–18.9 | Transactions: 19 → 708 with the biggest landing, rows reflow | whip with a slight roll | |
| 18.9–22.8 | **hold** — transactions | — | |
| 22.8–25.6 | Digital maturity: the star yields, four rings draw around it (54 / 15 / 52 / 46 %), cells become the four dimensions, bars split into four colours | push into the rosette | rings fold back into the star |
| 25.6–28.8 | **hold** — digital | — | |
| 28.8–30.1 | rings unwind, cards lift away, the star travels home and the cream closes into it | iris closes | the star on black |
| 30.1–34 | شكراً لكم · ministry · date · **hold** | — | end |

## Colours (sampled from the PDF)

| token | hex | use |
|---|---|---|
| gold | `#d9a86a` | totals, the star, lattice |
| navy | `#174766` | مكتملة |
| green | `#038060` | على المخطط |
| brown | `#87452b` | متأخرة |
| grey | `#a6a6a6` | معلقة / لم تبدأ |
| tabs | `#111111` · `#004545` · `#1f4d6b` · `#c99a5c` | tasks · Suhail · transactions · digital (pill + page band) |
| dimensions | `#d0a062` · `#0b524a` · `#9b5530` · `#66a5ce` | user experience · beneficiary satisfaction · complaints · tech & tools |
| page | `#fbf7f4` on Kiswa black `#0b0a09` | |

Type: IBM Plex Sans Arabic (text, numbers) and Amiri (the closing line), both SIL OFL, inlined in `faces.css`.

## Sound

`score.py` reads `window.__events()` and places the synthesised palette in one room; struck-glass tones are tuned to
a Hijaz scale on D. No music track — add a licensed one if wanted.

## Files

- `comp.html` — the composition (`?play` to preview, `?t=12.3` to pin a frame)
- `motion.js` — the library copy; `faces.css` — the fonts
- `score.py` → `sfx.wav`
- `mohu-weekly.mp4` — 1080×1920 · 30 fps draft with shutter motion blur

```bash
python3 scripts/render.py cases/mohu-weekly-32s/comp.html --out cases/mohu-weekly-32s/mohu-weekly.mp4 \
  --sfx cases/mohu-weekly-32s/sfx.wav --width 1080 --height 1920 --workers 4 --samples-max 16 --gap 10
# final: add --final (2× scale, 60 fps)
```

To update for next week, edit the `SEC` table (totals, cells, rows per sector, highlights) and the date strings.
