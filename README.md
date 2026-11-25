# One Star for Monday

A one-star review of Monday, written as though Monday were a restaurant:
Friday's order, served cold on Monday, with a bill for the weekend.

Built for the [make.fun](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61) bounty "One Star for Monday".

[![make.fun · u-clever-harbor-75-one-star-for-monday-9ead4a61](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/arsalive-dot/one-star-for-monday/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/arsalive-dot/one-star-for-monday/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)

## How it works

`main.py` (Python 3, standard library only) writes the review to
`/output/entry.txt` deterministically: it writes a temporary file, then
atomically replaces the final file and sets mode 644.
