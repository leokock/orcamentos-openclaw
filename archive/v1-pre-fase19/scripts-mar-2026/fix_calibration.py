#!/usr/bin/env python3
"""
Fix calibration-data.json (redentor pct bug) and regenerate calibration-stats.json.

Bug: redentor project has absolute R$ values in 'pct' fields instead of percentages.
Fix: recalculate pct = valor / total * 100 for any project where pct > 100.
Then regenerate all stats.
"""

import json
import statistics
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE, "calibration-data.json")
STATS_PATH = os.path.join(BASE, "calibration-stats.json")

# 1. Load and fix calibration-data.json
with open(DATA_PATH) as f:
    data = json.load(f)

fixed_projects = []
for p in data:
    cats = p.get("categories", {})
    total = p.get("total", 0)
    if not total:
        continue
    for cat, vals in cats.items():
        pct = vals.get("pct", 0)
        if pct > 100:
            correct_pct = round(vals.get("valor", 0) / total * 100, 4)
            vals["pct"] = correct_pct
            if p["name"] not in fixed_projects:
                fixed_projects.append(p["name"])

if fixed_projects:
    print(f"Fixed pct values for projects: {fixed_projects}")
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved fixed {DATA_PATH}")

# 2. Regenerate calibration-stats.json
from datetime import date

# Collect all category names
all_cats = set()
for p in data:
    all_cats.update(p.get("categories", {}).keys())

# Global stats
cub_ratios = [p["cub_ratio"] for p in data if p.get("cub_ratio")]
rsm2_vals = [p["rsm2"] for p in data if p.get("rsm2")]
ac_vals = [p["ac"] for p in data if p.get("ac")]

def calc_stats(values):
    if len(values) < 2:
        if len(values) == 1:
            return {"median": round(values[0], 4), "mean": round(values[0], 4),
                    "min": round(values[0], 4), "max": round(values[0], 4),
                    "stdev": 0, "n": 1}
        return None
    return {
        "median": round(statistics.median(values), 4),
        "mean": round(statistics.mean(values), 4),
        "min": round(min(values), 4),
        "max": round(max(values), 4),
        "stdev": round(statistics.stdev(values), 4),
        "n": len(values)
    }

stats = {
    "total_projects": len(data),
    "last_updated": date.today().isoformat(),
    "last_project": data[-1]["name"] if data else "",
    "global": {
        "cub_ratio": calc_stats(cub_ratios),
        "rsm2": calc_stats(rsm2_vals),
        "ac": calc_stats(ac_vals),
    },
    "categories": {}
}

# Remove stdev from global if present (original didn't always have it consistently)
# Actually keep it consistent

for cat in sorted(all_cats):
    pct_vals = []
    rsm2_vals_cat = []
    for p in data:
        c = p.get("categories", {}).get(cat)
        if c:
            pct = c.get("pct")
            rsm2 = c.get("rsm2")
            if pct is not None and 0 < pct <= 100:
                pct_vals.append(pct)
            if rsm2 is not None and rsm2 > 0:
                rsm2_vals_cat.append(rsm2)
    
    n = len(pct_vals) if pct_vals else len(rsm2_vals_cat)
    if n == 0:
        stats["categories"][cat] = {"n": 0}
        continue
    
    entry = {"n": n}
    if pct_vals:
        entry["pct"] = {
            "median": round(statistics.median(pct_vals), 4),
            "mean": round(statistics.mean(pct_vals), 4),
            "min": round(min(pct_vals), 4),
            "max": round(max(pct_vals), 4),
        }
    if rsm2_vals_cat:
        entry["rsm2"] = {
            "median": round(statistics.median(rsm2_vals_cat), 4),
            "mean": round(statistics.mean(rsm2_vals_cat), 4),
            "min": round(min(rsm2_vals_cat), 4),
            "max": round(max(rsm2_vals_cat), 4),
        }
    stats["categories"][cat] = entry

with open(STATS_PATH, "w") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

print(f"\nRegenerated {STATS_PATH}")
print(f"Total projects: {len(data)}")
print(f"Categories: {len(stats['categories'])}")
print("\nCategory medians (rsm2):")
for cat in sorted(stats["categories"].keys()):
    entry = stats["categories"][cat]
    rsm2 = entry.get("rsm2", {})
    pct = entry.get("pct", {})
    print(f"  {cat}: rsm2_median={rsm2.get('median', 'N/A')}, pct_median={pct.get('median', 'N/A')}, n={entry['n']}")
