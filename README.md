# Strategic Default Pressure Index: advance-funding risk in commodity finance

The index finds the market price at which a supplier, funded against a future delivery, gains more by selling elsewhere than by delivering.

For this book, that point is a 6.00% premium over the advance.

I carried this exposure personally, under bond, as the franchise holder funding 36 purchasing clerks in a Ghanaian cocoa district. I built the index while running that book.

The funding policy behind it is mine too: a risk tier for each clerk, and funding ceilings based on averages.

This piece rebuilds the 2022/23 season from the operational records, week by week.

## Why it matters

Most commodity buying at origin is financed by advances against future delivery.

Lenders usually deal with default after the event: a delivery fails, the loss is booked and the recovery work starts.

Yet a supplier decides to default before the delivery date, on prices the lender can see too.

The index tracks how close the market premium is to the point where default pays, and flags the clerks whose positions are most exposed to it.

## The data

One cocoa franchise district in the 2022/23 season: 36 purchasing clerks over 16 weeks, from 16 September to 30 December 2022.

Three dated risk reports cover the same season. The position can be followed through the weeks, as well as at the close.

## What it found

### 1. Default pays above a 6.00% premium

A supplier who takes the advance and sells elsewhere loses 6.00% of the GHS 800 bag price. In 2022/23 that was GHS 48.

Above that premium, default pays.

### 2. The open gap fell 83% from its peak

| Report | Clerks | Funded | Delivered | Open gap | Recovery | Net exposure (GHS) |
|---|---:|---:|---:|---:|---:|---:|
| Opening | 35 | 1,487 | 1,190 | 297 | 80.0% | 169,788 |
| November | 36 | 2,025 | 1,798 | 227 | 88.8% | 87,124 |
| December | 36 | 2,075 | 1,964 | 111 | 94.7% | −9,468 |

Open exposure peaked at 654 bags in the week ending 25 November and closed the season at 111 bags, while the funding kept growing.

In money, GHS 169,788 of open exposure at the opening report became a GHS 9,468 credit sixteen weeks later, on a book that funded GHS 1.66 million over the season.

The bond was never drawn on.

### 3. Four clerks carried half the exposure

Four of the 36 clerks carried half of the open gap. Nine carried 80%. The largest single position was 19.5% of the total.

One funding policy for all 36 would have mispriced almost all of them.

The district's written policy already placed clerks in risk tiers. The season data puts numbers on them.

## Where the pressure came from

COCOBOD sets one producer price for the whole season, so a Ghanaian supplier has no domestic spot market to sell into. In 2022/23 it was GHS 800 per 64 kg bag from 7 October 2022, the figure the model uses.

The pressure came from across the border, and from the currency.

| Reference, 2022/23 | Price | In US dollars (the CFA franc is pegged to the euro) |
|---|---|---|
| Ghana, COCOBOD price | GHS 800 / 64 kg = GHS 12.50/kg | $0.89 to $1.25/kg, falling through the season with the cedi |
| Côte d'Ivoire, farmgate price | 900 CFA/kg | about $1.33/kg, roughly flat |

The cedi lost about 27% against the dollar in 2022, touching about GHS 14.6 to the dollar late in the year.

As it fell, the Ivorian price moved further above Ghana's in dollar terms. Roughly level early in the season, it was 40 to 50% higher at the cedi's low point.

A supplier defaults when selling elsewhere nets more than 6% over the advance. For much of the season the cross-border gap ran at several times that threshold, and Ghana lost significant volume to smuggling into Côte d'Ivoire that year.

The season data has the same shape. The open gap was widest at the opening report, 297 bags with 80% recovery, just as the cross-border gap was opening, and it came down only through active recovery.

## Limits

The data shows the direction and size of the pressure. It cannot date the week a given clerk crossed the threshold; that would need a daily cedi to dollar series and the costs of the smuggling routes, including transport, risk and the discount a cross-border buyer takes.

Cross-border prices set an upper bound on the pressure, because smuggling carries its own cost and risk and most suppliers never do it.

So the index measures the incentive to default, which a lender can act on before a delivery fails.

This is one district over one season. It is a reconstruction from operational records at weekly frequency, because the business reported weekly, and it is not a production risk system.

## Price reference

| Season | COCOBOD producer price (Ghana, 64 kg bag) | Côte d'Ivoire farmgate price |
|---|---|---|
| 2021/22 | GHS 660 | 825 CFA/kg (main crop) |
| 2022/23 | GHS 800 (from 7 October 2022) | 900 CFA/kg (about $1.33/kg) |

Sources: [COCOBOD: producer price up 21% to GH¢800/bag](https://cocobod.gh/news/cocoa-producer-price-goes-up-21-to-gh800-per-bag) ·
[COCOBOD: 2021/22 price maintained](https://cocobod.gh/news/government-maintains-cocoa-producer-price-for-the-20212022-crop-year) ·
[Ivory Coast raises 2022/23 farmgate price 9% to 900 CFA](https://furtherafrica.com/2022/10/03/ivory-coast-raises-cocoa-farmgate-price-by-9-for-2022-2023-harvest/) ·
[GHS/USD exchange rate history, 2022](https://www.exchange-rates.org/exchange-rate-history/ghs-usd-2022).

## Running it

```bash
python sdpi.py --data data --figures
```

The `--figures` option needs matplotlib. The results print without it.
