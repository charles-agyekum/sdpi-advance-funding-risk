# Strategic Default Pressure Index: advance-funding risk in commodity finance

**The question.** When you lend against a future delivery, at what market price does your
counterparty profit by not delivering?

**The answer, for this book.** A 6.00 % premium. Above it, a supplier earns more by selling
elsewhere and forfeiting the collateral than by honouring the advance.

**Whose book.** Mine. I carried this exposure personally, under bond, as the franchise holder
funding 36 purchasing clerks across a Ghanaian cocoa district. I built the index while running
that book, because the losses were mine to absorb. The written funding policy behind these
numbers is also mine: clerk risk-tiering and averaging-based funding ceilings.

So the risk here was real before it was ever analytical. This piece reconstructs the season
from the operational records and shows what the index was doing.

---

## Why it matters

Advance-against-delivery is how most origin commodity trade is financed. The exposure is
usually managed **reactively**: a delivery fails, the loss is booked, recovery starts. But
the decision to default is an economic one, made by the counterparty before the delivery date,
and the inputs to that decision are all observable in advance.

So the exposure is predictable. The index makes the prediction explicit: it tracks how close
the market premium is to the point where defaulting becomes the rational choice, and flags
the counterparties whose position makes them most sensitive to it.

That is the shift the piece demonstrates: **from booking losses to pricing the incentive
that causes them.**

## The data

One cocoa franchise district, 2022/23 season. **36 purchasing clerks, 16 weeks**
(16 Sep to 30 Dec 2022), from three dated risk reports that track the same season
forward, so the position itself has a time dimension, not just a closing snapshot.

## What it found

**1. The threshold is 6.00 %, and it is exact.**

**2. The gap closed by 83 % over the season.**

| Report | Clerks | Funded | Delivered | Open gap | Recovery | Net exposure (GHS) |
|---|---:|---:|---:|---:|---:|---:|
| Opening | 35 | 1,487 | 1,190 | 297 | 80.0 % | 169,788 |
| November | 36 | 2,025 | 1,798 | 227 | 88.8 % | 87,124 |
| December | 36 | 2,075 | 1,964 | 111 | 94.7 % | **−9,468** |

Peak open exposure was **654 bags in the week ending 25 November**, closing at 111, an 83 %
reduction *while funding continued to grow*, which is the harder version of the problem. By
season end the net position had crossed into credit.

In money: **GHS 169,788 of open exposure recovered to a GHS 9,468 credit** across sixteen
weeks. On a book that funded GHS 1.66 million over the season, that is the difference between
a written-off season and a clean one, and it was recovered without withdrawing the bond.

**3. Exposure was concentrated, not spread.**

**4 of 36 clerks carried half the open gap; 9 carried 80 %.** The largest single position was
19.5 % of the total on its own.

This is the finding with the clearest operational consequence. A uniform funding policy
across 36 counterparties would have mispriced almost all of them. The district's own written
policy already categorised clerks; the data supports that judgement and quantifies it.

## The market side: where the default pressure actually comes from

The archive holds no price column, so an early draft of this piece said the index "could not
be shown firing against live prices." That was too pessimistic, and it misread the market.
Ghana's cocoa price is **administered, not floating**. COCOBOD fixes a single producer price
for the whole season, so there is no domestic spot market for a supplier to sell into. The
2022/23 price was set at **GH¢800 per 64 kg bag** from 7 October 2022, which is exactly the
`800` the archive's model runs on. The season data and the official price agree.

So the default pressure is not a rising *domestic* price. It is **cross-border and currency
arbitrage**:

| Reference, 2022/23 | Price | In USD (CFA is euro-pegged and stable) |
|---|---|---|
| Ghana, COCOBOD fixed | GH¢800 / 64 kg = **GH¢12.50/kg** | **$0.89 to $1.25/kg**, falling through the season as the cedi did |
| Côte d'Ivoire, fixed farmgate | **900 CFA/kg** | **~$1.33/kg**, roughly flat |

The Ghanaian cedi **lost about 27% against the dollar in 2022**, touching ~GH¢14.6/$ late in
the year. As it fell, the Ivorian farmgate price pulled further above the Ghanaian one in real
terms, from roughly level early in the season to **~40 to 50% higher** by its trough.

**Set that against the index's 6.00% threshold.** A supplier defaults when they can net more
than 6% elsewhere. For much of the 2022/23 season the cross-border gap **exceeded that
threshold by several times**, which is precisely why Ghana lost significant volume to
smuggling into Côte d'Ivoire that year. The index was not a hypothesis; the pressure it
measures was real and, in this season, severe. It also explains the archive's own shape: the
default gap was **widest early** (297 bags, 80% recovery at the opening report) when the
arbitrage was opening up, and was worked down only through active recovery.

## What it still does not show

The **direction and magnitude** of the pressure are now evidenced and sourced. What is not
derivable to the day is the exact date the threshold was crossed for a given clerk; that
needs a **daily** cedi/dollar series and the specific smuggling-route economics (transport,
risk, the discount a cross-border buyer pays), none of which are in the archive.

And the honest ceiling on the claim: the cross-border price is an **upper bound on pressure**,
not a realised return every supplier could capture. Smuggling carries cost and risk, and most
suppliers never act on it. The index measures *pressure to default*, which is what its name
says, not a guaranteed alternative price. That is the right thing for a risk instrument to
measure: the incentive, before the delivery fails.

## Price reference

| Season | COCOBOD producer price (Ghana, 64 kg bag) | Côte d'Ivoire farmgate |
|---|---|---|
| 2021/22 | GH¢660 | 825 CFA/kg (main crop) |
| 2022/23 | **GH¢800** (from 7 Oct 2022) | 900 CFA/kg (~$1.33/kg) |

Sources: [COCOBOD: producer price up 21% to GH¢800/bag](https://cocobod.gh/news/cocoa-producer-price-goes-up-21-to-gh800-per-bag) ·
[COCOBOD: 2021/22 price maintained](https://cocobod.gh/news/government-maintains-cocoa-producer-price-for-the-20212022-crop-year) ·
[Ivory Coast raises 2022/23 farmgate price 9% to 900 CFA](https://furtherafrica.com/2022/10/03/ivory-coast-raises-cocoa-farmgate-price-by-9-for-2022-2023-harvest/) ·
[GHS/USD 2022 history (−26% on the year)](https://www.exchange-rates.org/exchange-rate-history/ghs-usd-2022).

Other limits worth being straight about: one district, one season, 36 counterparties. A
reconstruction from operational records, not a production risk system. Weekly granularity,
because that is the reporting cadence the business ran on.

## Running it

```bash
python sdpi.py --data data --figures
```

## Where this sits

| | |
|---|---|
| Method | Python · district-level aggregation · incentive-threshold derivation |
| Domain | Commodity finance · counterparty credit risk · advance-against-delivery |
