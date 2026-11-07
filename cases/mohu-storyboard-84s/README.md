# mohu-storyboard — لوحة القصة القيادية · 84 s, vertical 1080×1920

The executive storyboard for the weekly achievement report (5 November 2026), built shot for shot: 11 scenes,
84 seconds, 9:16, the report's colours. Following the storyboard there is **no decorative star** and **no voice-over**.
Sound is only a swipe at each scene transition, with no bells.

**Concept: one gold line carries the film.** It underlines the report title. It widens, and the cream page opens from it.
It becomes the status axis beside the three tracks, then splits into the two task numbers (completed in navy, on
plan in green). The completed part becomes the edges of the two achievement cards. The card edges gather into the
Suhail counter, which extends into the edges of the project-update cards. One edge runs into the transactions strip,
which branches into the four maturity rings. The rings merge into one line, and that line opens the Nusuk tracks,
sets the three priorities, and finally gathers under the closing line as the page closes back onto black.

| # | t (s) | scene | the line |
|---|---|---|---|
| 01 | 0–4 | الافتتاح: the title on Kiswa black | draws under «الأسبوعي» |
| 02 | 4–9 | مؤشرات التنفيذ: three tracks, no delays | widens, opens the page, becomes the status axis |
| 03 | 9–16 | ملخص المهام: 22 · 2 مكتملة · 20 على المخطط | splits into navy 2 / green 20 |
| 04 | 16–24 | منجزات الأسبوع: the two completed tasks | becomes the two card edges |
| 05 | 24–31 | مشاريع سهيل: 19 · 6 · 13 | the edges gather into navy 6 / green 13 |
| 06 | 31–41 | مستجدات المشاريع | extends into the two card edges |
| 07 | 41–48 | المعاملات: 708 · 402 · 306 | one edge becomes navy 402 / green 306 |
| 08 | 48–63 | نضج التجربة الرقمية: 54 · 52 · 46 · 15 % | branches into the four rings |
| 09 | 63–70 | التجربة الرقمية: development tracks | the rings merge into one line, then the card edges |
| 10 | 70–79 | أولويات المتابعة: 01 · 02 · 03 | becomes the three priority bars |
| 11 | 79–84 | الخاتمة on Kiswa black | gathers under «لخدمة ضيوف الرحمن» |

The accuracy rules in the storyboard are kept. The percentages are labelled only as completion rates of the
maturity-index requirements. The visa item reads as an agreement to study, and the Nusuk unification reads as work
in progress. The main tracks show no delays.

The opening and the closing use the report's cover photograph (`kaaba.jpg`: the Kiswa and the door), darkened and faded to black under the type. Scene 04 carries the full text of the two completed tasks from page 2 of the report: the task, the sector and the note.

Files: `comp.html` (`?play`, `?t=12.3`), `motion.js`, `faces.css` (IBM Plex Sans Arabic, OFL), and `score.py` → `sfx.wav`,
which places swipes at the transitions only. `kaaba.jpg` is the report's cover photograph; `logo_light.png` (from the cover) and `logo_dark.png` (the same, ink text for the cream page) are the ministry logo in the header and the closing. The video is `mohu-storyboard.mp4`, a 30 fps draft with shutter motion blur.

```bash
python3 scripts/render.py cases/mohu-storyboard-84s/comp.html --out cases/mohu-storyboard-84s/mohu-storyboard.mp4 \
  --sfx cases/mohu-storyboard-84s/sfx.wav --width 1080 --height 1920 --workers 4 --samples-max 8 --gap 16
```
