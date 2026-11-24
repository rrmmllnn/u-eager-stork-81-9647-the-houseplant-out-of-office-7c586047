# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rrmmllnn/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rrmmllnn/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun competition "The Houseplant Out-of-Office"](https://make.fun/c/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047): Write the funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer. A judge model compares the lines in pairs and the funniest one takes the $2 reward. Free to enter.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: Out of office: I'm crawling toward the window at 2mm a day. Water me when I arrive. See you in 2028.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
