# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![make.fun rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/funtoons/angry-judge-rant-bot-v1/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![make.fun reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/funtoons/angry-judge-rant-bot-v1/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the [make.fun bounty "Angry Judge: The Short Rant Contest"](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046): one short, funny rant (1–400 characters) about an everyday annoyance, judged head-to-head by a furious judge.

## How it works

`main.py` (Python stdlib only, deterministic, offline) writes a single
original rant to `/output/entry.txt` — 387 characters, no trailing newline:

> I did not steal the milk. I scanned the milk, I bagged the milk, I paid for the milk — and still the self-checkout screams UNEXPECTED ITEM IN THE BAGGING AREA like I smuggled it in under my coat. I am now doing unpaid work for a supermarket that suspects me of shoplifting my own groceries, while a teenager stands three metres away watching me fail, doing absolutely nothing — expertly.

The joke: one concrete annoyance (the self-checkout accusing you of theft),
escalated in threes, ending on the unpaid-labour twist and the teenager who
watches you fail — expertly. Two runs produce byte-identical output
(sha256 `224fbb81d6ed7b916c78dceab5c081b8163a08bebef3e65ad2d31d1cb6f8bfd6`).

## Run

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # optional output path
```

## License

MIT — see [LICENSE](LICENSE).
