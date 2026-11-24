# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/asfel307/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/asfel307/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

## The World Today — Tuesday, 24 November 2026

A single front-page newspaper infographic summing up the world's news for
Tuesday, 24 November 2026. One lead story on Jensen Huang returning as
Nvidia CEO and the stock's 31% surge, plus five more stories: a deadly
candy-factory fire in Cikande, Indonesia; a Russian strike on the Kyiv
region; the COP31 climate talks ending without a deal; Carlos Alcaraz
winning his first ATP Finals title; and the World Chess Championship
match between Gukesh and Sindarov opening in Geneva.

The image is drawn entirely in code with Pillow: warm cream paper, dark
slate ink, dark-teal and gold accents, a big serif masthead, and a small
pictogram for every story — a chip, a factory, a missile, a globe, a
trophy, and a chess king. No photos, no downloaded assets, no network
calls anywhere in the build.

## The six stories

The front page is dated Tuesday, 24 November 2026 and was compiled in the
early hours of that day (UTC). The events themselves took place on 22–24
November, with fresh developments reported on 24 November — market moves,
casualty updates, and the championship opening on Tuesday morning. Each
story was checked against wire reporting before it was drawn.

1. **Lead — Jensen Huang returns as Nvidia CEO; shares surge 31%.**
   Nvidia's stock jumped 31% — its best day since 2003 — after Jensen
   Huang returned as chief executive, easing uncertainty after a sharp
   sell-off; the Nasdaq rose 6.5%.
   Sources: Reuters / CNN.
   https://www.briefing.com/story-stocks/archive/2026/11/23/nvidia-surges-as-jensen-huang-returns-as-ceo-easing-uncertainty-following-sharp-selloff-(nvda)
2. **Factory fire in Cikande, Indonesia kills 24.**
   A fire at a candy factory in Cikande, Banten, killed 24 people, with
   around 30 still missing as rescuers searched the wreckage.
   Source: Reuters via TBS News.
   https://www.tbsnews.net/worldbiz/asia/indonesia-says-24-killed-factory-blaze-rescuers-search-dozens-missing-1611156
3. **Russian strike on Kyiv region kills at least 12.**
   A Russian attack on the Kyiv region killed at least 12 people, hitting
   an apartment block in Dymer, a supermarket in Vyshneve, and homes in
   Bila Tserkva.
   Sources: Reuters / RTÉ.
   https://www.europesays.com/russia/93107/
4. **COP31 ends without a deal.**
   After more than 44 hours of overtime, the COP31 climate talks in
   Antalya ended with no agreement. The EU and other countries rejected a
   final draft that made no mention of fossil fuels. COP president Murat
   Kurum conceded there was no consensus. It was the longest COP in
   history.
   Source: NPR.
   https://www.nprillinois.org/2026-11-22/climate-change-talks-fall-apart-in-final-hours-over-fossil-fuels
5. **Alcaraz wins his first ATP Finals title.**
   Carlos Alcaraz beat Alexander Zverev 6-2, 7-6(7) in Turin to win the
   Nitto ATP Finals for the first time.
   Source: ATP Tour.
   https://www.atptour.com/en/news/alcaraz-zverev-nitto-atp-finals-2026-sunday
6. **World Chess Championship opens in Geneva.**
   Game 1 of the FIDE World Championship match between Gukesh Dommaraju
   and Javokhir Sindarov — the youngest final in history, 14 games, a
   $2.5 million prize fund — began today in Geneva.
   Source: ChessBase India.
   https://chessbase.in/news/fide-world-championship-match-2026-preview-report

## How it works

`render.py` draws the front page with Pillow and writes `entry.png`
(1024×1024, under 1 MiB). `main.py` (Python standard library only) copies
`entry.png` byte for byte to the make.fun output directory, so both runs
produce identical bytes:

```sh
python3 render.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
