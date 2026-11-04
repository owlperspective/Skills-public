#!/usr/bin/env python3
"""Generate Finviz CANSLIM-style screener URLs.

This helper does not scrape Finviz. It builds repeatable first-pass screen URLs
that should be validated with current filings, available market data, and chart review.
"""

from __future__ import annotations

import argparse
from urllib.parse import urlencode


FILTERS = {
    "balanced": [
        "fa_eps5years_o15",
        "fa_epsqoq_o25",
        "fa_epsyoy_o25",
        "fa_opermargin_pos",
        "fa_roe_o15",
        "fa_salesqoq_o25",
    ],
    "strict": [
        "fa_eps5years_o25",
        "fa_epsqoq_o25",
        "fa_epsyoy_o25",
        "fa_opermargin_pos",
        "fa_roe_o20",
        "fa_salesqoq_o25",
        "sh_avgvol_o500",
        "sh_price_o10",
        "ta_sma50_pa",
        "ta_sma200_pa",
    ],
    "early": [
        "fa_epsqoq_o25",
        "fa_epsyoy_o25",
        "fa_opermargin_pos",
        "fa_salesqoq_o25",
        "sh_avgvol_o300",
        "sh_price_o10",
    ],
}


def build_url(mode: str, preset: str | None) -> str:
    params = {
        "v": "111",
        "f": ",".join(FILTERS[mode]),
        "ft": "4",
    }
    if preset:
        params["preset"] = preset
    return "https://finviz.com/screener?" + urlencode(params)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Finviz CANSLIM screener URL.")
    parser.add_argument("--mode", choices=sorted(FILTERS), default="balanced")
    parser.add_argument(
        "--preset",
        default=None,
        help="Optional user-supplied Finviz preset ID.",
    )
    args = parser.parse_args()
    print(build_url(args.mode, args.preset))


if __name__ == "__main__":
    main()
