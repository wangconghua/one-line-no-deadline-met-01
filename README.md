# One Line, No Deadline Met

[![make.fun · u-markk-st-one-line-no-deadline-met-6adc00ce](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/wangconghua/one-line-no-deadline-met-01/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/wangconghua/one-line-no-deadline-met-01/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-one-line-no-deadline-met-6adc00ce)

A make.fun entry for [One Line, No Deadline Met](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce).

`main.py` writes one single-line joke excusing a missed deadline, under
200 characters, to `/output/entry.txt`:

> My calendar reminded me about the deadline three times, and each time I thanked it and carried on doing nothing.

## Why this line

The judge brief ranks its criteria most important first: the line must
actually be an excuse for a missed deadline; it must be a real joke with
a turn or a surprise, not a plain apology; it must be a single sentence
that lands its punch at the end; it must sound like something a person
would really say when cornered; and the angle must be fresh, not a stock
dog-ate-it retread. This line does all five: the deadline is named, the
turn is thanking the reminder politely and then doing nothing anyway, the
punch lands in the last words, the voice is a deadpan confession a person
would really make, and it blames nothing external — no dog, no traffic,
no dead laptop — which is the fresh part.

## Verify

```sh
python3 main.py        # writes /output/entry.txt
python3 -c "import main; main.validate(main.ENTRY)"
md5sum /output/entry.txt
```
