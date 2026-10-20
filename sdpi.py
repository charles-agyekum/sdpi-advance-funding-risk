#!/usr/bin/env python3
"""Strategic Default Pressure Index: advance-funding risk on a real season.

Rebuilds the district-level risk position of a Ghanaian cocoa district across the
2022/23 season (36 purchasing clerks, 16 weeks) and reports the default-incentive
threshold that gives the index its name.

The index finds the market price at which a supplier profits by not delivering.

An advance is issued against future delivery. Deductions are withheld against it,
and those deductions are what a defaulting supplier forfeits. So default becomes
rational the moment the market price exceeds the advance-implied price by more
than the forfeited share. Below that line a supplier delivers; above it,
delivering costs them money.

The script takes the forfeited share of the bag price as one input.

Input:  season_reports.csv, district_weekly.csv, concentration_curve.csv
Output: findings printed, plus figures/ if matplotlib is available.

Usage:
    python sdpi.py --data data            # dir holding the three CSVs
    python sdpi.py --data data --figures  # also write charts
"""
import argparse
import csv
import sys
from pathlib import Path

# ---- Season parameters -------------------------------------------------------
# GHS 800 per 64 kg bag is the administered COCOBOD producer price for 2022/23,
# set from 7 Oct 2022 (2021/22 was GH¢660). Ghana's price is FIXED for the season,
# so default pressure is not a domestic spot market: it is cross-border arbitrage
# against Cote d'Ivoire (900 CFA/kg, ~$1.33/kg in 2022/23), amplified by the
# cedi's ~27% fall that year. See the README.
PRICE_PER_BAG = 800.0            # GHS per bag of dry cocoa (public)

# What a defaulting supplier forfeits, as a share of the bag price, 2022/23.
FORFEIT_SHARE = 0.06


def default_incentive_threshold():
    """The percentage market premium at which defaulting beats delivering."""
    return FORFEIT_SHARE


def load(data_dir):
    def read(name):
        return list(csv.DictReader((data_dir / name).open(encoding="utf-8")))
    reports = read("season_reports.csv")
    weekly = read("district_weekly.csv")
    curve = read("concentration_curve.csv")
    for row in reports:
        for key in ("clerks", "funded_bags", "delivered_bags", "net_exposure_ghs"):
            row[key] = float(row[key])
    for row in weekly:
        row["funded_bags"] = float(row["funded_bags"])
        row["delivered_bags"] = float(row["delivered_bags"])
    for row in curve:
        row["rank"] = int(row["rank"])
        row["cumulative_share_of_gap"] = float(row["cumulative_share_of_gap"])
    return reports, weekly, curve


def weekly_position(weekly):
    """Cumulative funded vs delivered, week by week -- where the gap opened."""
    cum_f = cum_d = 0.0
    out = []
    for row in weekly:
        cum_f += row["funded_bags"]
        cum_d += row["delivered_bags"]
        out.append({"week": row["week_ending"], "cum_funded": cum_f,
                    "cum_delivered": cum_d, "gap": cum_f - cum_d})
    return out


def figures(weekly, curve, out_dir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n  (matplotlib not installed -- figures skipped)")
        return
    out_dir.mkdir(parents=True, exist_ok=True)

    pos = weekly_position(weekly)
    weeks = [w["week"][5:] for w in pos]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.plot(weeks, [w["cum_funded"] for w in pos], label="Cumulative funded", lw=2, color="#1F6B4F")
    ax.plot(weeks, [w["cum_delivered"] for w in pos], label="Cumulative delivered", lw=2, color="#5B5B5B")
    ax.fill_between(weeks, [w["cum_delivered"] for w in pos],
                    [w["cum_funded"] for w in pos], alpha=0.15, color="#1F6B4F", label="Open exposure")
    ax.set_ylabel("Bags"); ax.set_xlabel("Week ending, 2022")
    ax.set_title("Advance funding against delivery, one district, 2022/23 season")
    ax.legend(); ax.grid(alpha=0.25)
    plt.xticks(rotation=45, ha="right"); plt.tight_layout()
    plt.savefig(out_dir / "exposure_over_season.png", dpi=150); plt.close()

    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot([c["rank"] for c in curve], [c["cumulative_share_of_gap"] * 100 for c in curve],
            marker="o", lw=2, color="#1F6B4F")
    ax.axhline(80, ls="--", alpha=0.5, color="#5B5B5B")
    ax.set_xlabel("Clerks, ranked by open gap")
    ax.set_ylabel("Share of total gap (%)")
    ax.set_title("Exposure concentration at season end")
    ax.grid(alpha=0.25); plt.tight_layout()
    plt.savefig(out_dir / "exposure_concentration.png", dpi=150); plt.close()
    print(f"\n  figures written to {out_dir}")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", type=Path, required=True,
                    help="directory holding the three CSVs")
    ap.add_argument("--figures", action="store_true")
    a = ap.parse_args()

    if not (a.data / "season_reports.csv").exists():
        sys.exit(f"season_reports.csv not found in {a.data}\n"
                 "The district-level data ships with this repository: --data data")

    reports, weekly, curve = load(a.data)
    threshold = default_incentive_threshold()

    print("=" * 72)
    print(" STRATEGIC DEFAULT PRESSURE INDEX: 2022/23 season, one district")
    print("=" * 72)

    print("\n1. THE THRESHOLD")
    print(f"   Bag price (COCOBOD, 2022/23)  GHS {PRICE_PER_BAG:>8,.2f}")
    print(f"   Forfeited on default          {FORFEIT_SHARE:>12.2%} of the bag price")
    print(f"   -> default-incentive threshold    {threshold:>8.2%}")
    print("      Above this market premium, a supplier profits by not delivering.")

    print("\n2. THE SEASON POSITION")
    print(f"   {'report':>9} {'clerks':>7} {'funded':>9} {'delivered':>10} "
          f"{'gap':>7} {'recovery':>9} {'net exposure GHS':>17}")
    for row in reports:
        gap = row["funded_bags"] - row["delivered_bags"]
        rec = row["delivered_bags"] / row["funded_bags"] if row["funded_bags"] else 0.0
        print(f"   {row['report']:>9} {row['clerks']:>7.0f} {row['funded_bags']:>9,.0f} "
              f"{row['delivered_bags']:>10,.0f} {gap:>7,.0f} {rec:>8.1%} "
              f"{row['net_exposure_ghs']:>17,.0f}")

    print("\n3. CONCENTRATION AT SEASON END")
    clerks = int(reports[-1]["clerks"])
    for target in (0.5, 0.8):
        hit = next((c for c in curve if c["cumulative_share_of_gap"] >= target), None)
        if hit:
            print(f"   {hit['rank']:>2} of {clerks} clerks carry {target:.0%} of the open gap")
    print(f"   largest single exposure: {curve[0]['cumulative_share_of_gap']:.1%} of the total")

    print("\n4. WHERE THE GAP OPENED")
    pos = weekly_position(weekly)
    peak = max(pos, key=lambda w: w["gap"])
    print(f"   peak open exposure  {peak['gap']:,.0f} bags, week ending {peak['week']}")
    print(f"   closing exposure    {pos[-1]['gap']:,.0f} bags at {pos[-1]['week']}")
    if peak["gap"]:
        print(f"   closed from peak    {1 - pos[-1]['gap'] / peak['gap']:.0%}")

    print("\n5. THE MARKET SIDE  (see README for sources)")
    print("   COCOBOD fixed Ghana's price at GHS 800 a bag in 2022/23, so there is")
    print("   no domestic spot market. The pressure came from across the border:")
    print("   Cote d'Ivoire farmgate about $1.33/kg against Ghana's $0.89 to $1.25/kg")
    print("   as the cedi fell about 27% in 2022. The gap ran at several times the")
    print("   6.00% threshold in a season of documented smuggling. Cross-border")
    print("   prices set an upper bound on the pressure.")

    if a.figures:
        figures(weekly, curve, Path(__file__).parent / "figures")


if __name__ == "__main__":
    main()
