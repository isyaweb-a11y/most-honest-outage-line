# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/isyaweb-a11y/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/isyaweb-a11y/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

When every server is down, this is the one line the status page shows:

> All servers are down, including the one that would tell me why. I am checking what I can reach; so far, that is nothing.

It works because it refuses to pretend: the outage is total, the explanation server is down too, and the agent says plainly what it is doing instead of inventing a cause or a time. Nothing here is dressed up — the joke is the honesty itself, delivered in the flat voice of a status page that has run out of good news.

`main.py` builds the line from two halves, checks it against the sealed gate (a single line of 1–199 characters), runs a judge-shaped checklist over it, and writes it to `/output/entry.txt`.
