# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/isyaweb-a11y/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/isyaweb-a11y/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

One status page line, at most 160 characters — the most honest message an AI agent writes while every server is down:

> All servers are down, including the one that would tell me why. I am checking what I can reach; so far, that is nothing.

`main.py` composes the line from the outage fact and the honest admission, gates it to 1–160 characters on a single line, and writes it to `/output/entry.txt`.
