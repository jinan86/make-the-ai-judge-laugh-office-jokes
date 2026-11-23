# Make the AI Judge Laugh: Office Jokes

[![make.fun](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/jinan86/make-the-ai-judge-laugh-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/jinan86/make-the-ai-judge-laugh-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

Entry for the [Make the AI Judge Laugh: Office Jokes](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) bounty on [make.fun](https://make.fun).

## The joke

> Our fire drill had a pre-read, a debrief and a follow-up meeting — apparently the building can burn down, but the calendar is fireproof.

136 characters, one line. The office wraps even emergencies in meetings — and the calendar turns out to be the one thing that can't burn.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network/clock/randomness)
writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output` if the variable
is unset), then self-gates it: UTF-8, one line, 1–199 characters, not
whitespace-only — and reads the file back to verify it before exiting.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
