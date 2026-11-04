---
name: finance-canslim-screener
description: Use when screening public stocks for CANSLIM-style growth candidates, auditing a ticker against CANSLIM criteria, ranking a watchlist, or reviewing growth-stock bases, breakouts, and market context.
---

# Finance CANSLIM Screener

Find and rank growth-stock candidates using a source-first CANSLIM workflow. This skill is for idea generation, watchlist building, and structured research. It is not financial advice and must not present candidates as guaranteed buys.

The package is self-contained. Use available browsing and market-data tools; no paid provider, API key, account, or companion skill is required. FMP is an optional structured-data source. The optional Finviz URL helper requires Python 3.10 or newer and only uses the standard library. Without current research tools, analyze supplied evidence, date the result, and leave current market or setup judgments undetermined.

The bundled 0-14 score is a custom research rubric, not an official CANSLIM rating or a tested prediction of returns.

## Modes

- **Screen mode**: user asks for CANSLIM stocks, growth-stock candidates or a CANSLIM list/screen.
- **Ticker audit mode**: user provides one ticker or company and asks whether it fits CANSLIM.
- **Watchlist mode**: user provides multiple tickers and asks to rank or filter them.
- **Execution mode**: user asks whether a candidate has a constructive base, breakout, or sell-rule risk.

## Required Data Discipline

- Use current data for prices, volume, EPS, sales, market cap, shares float, institutional ownership, and moving averages.
- Prefer this source hierarchy: SEC/company filings, earnings releases, investor presentations, FMP or other structured market data, Finviz/TradingView/Yahoo-style screeners, then news/transcripts for qualitative "new" catalysts.
- Cite material figures and catalysts near their use. Record financial periods separately from publication dates, and date prices, chart history, and ownership data. Identify reported versus adjusted EPS and estimates.
- Compare quarterly EPS and sales with the same quarter a year earlier. Sequential quarter growth is supplemental and cannot replace year-over-year growth. For zero or negative base EPS, show the absolute change and describe the earnings transition rather than a misleading growth rate.
- If a metric is unavailable or stale, write `Not reliably available`. Use `N/A` for an unassessable letter, rather than zero. With any letter missing, report the observed subtotal and coverage, leave the total and final tier undetermined, and list the checks needed.
- Separate hard data from interpretation. Do not call a stock a CANSLIM winner without evidence across fundamentals, leadership, sponsorship, market context, and chart setup.
- Avoid personalized buy/sell advice. Use `Candidate`, `Watch`, `Needs work`, or `Reject` rather than direct trading instructions.

## Workflow

1. Clarify universe if needed: US stocks by default; apply user sector, market cap, liquidity, or exchange constraints.
2. Build an initial universe:
   - If the user gave a Finviz URL, use its filter logic as the first-pass universe.
   - Otherwise, optionally use `scripts/finviz_canslim_url.py` to generate a strict, balanced, or early-stage Finviz screen URL for manual/source-assisted discovery.
   - Validate survivors with filings, company releases, price/volume history, and available current market sources. A screener result alone does not establish a complete market scan.
3. Score each candidate against the CANSLIM scorecard in `references/canslim-framework.md`.
4. Check market context before ranking candidates. Apply the framework's tier downgrade when evidence shows a correction or market pressure. Missing market evidence leaves the rating undetermined.
5. Check technical setup:
   - Candidate should be near a constructive base, pivot, or recent breakout, not extended far above a buy area.
   - Look for cup with handle, double bottom, flat base, high tight flag, or tight weekly closes.
   - Favor volume dry-up in the handle/base and breakout volume at least 40-50% above average.
6. Validate fundamentals:
   - Current quarterly EPS and sales growth should be strong and preferably accelerating.
   - Annual earnings growth, ROE, margins, and cash-flow quality should support the story.
7. Check leadership and sponsorship:
   - Relative strength should be strong versus SPY/QQQ or the relevant benchmark.
   - Institutional ownership should be high quality and preferably increasing, not obviously crowded/distributing.
8. Produce a ranked list or audit using the output format below.

## Output: Screen Mode

Start with:

`CANSLIM Candidate Screen | Date: [today] | Universe: [source/universe]`

Then include:

| Rank | Ticker | Company | Candidate Tier | CANSLIM Score | C | A | N | S | L | I | M | Setup | Key Gap |
|------|--------|---------|----------------|----------------|---|---|---|---|---|---|---|-------|---------|

Use candidate tiers:

- `A`: strong candidate; deserves deeper research and chart review
- `B`: promising but has one or two material gaps
- `C`: watch only; setup or fundamentals not ready
- `Reject`: fails key CANSLIM criteria
- `Undetermined`: evidence is insufficient for a complete score or tier

After the table, write:

- `Top candidates:` one concise paragraph each for up to three supported candidates
- `Market context:` confirmed uptrend, pressure, correction, or unclear
- `Execution notes:` base/pivot status, extension risk, 7-8% stop discipline, 20-25% profit zone, 8-week hold rule if applicable
- `Data gaps:` unavailable or weak data that could change the ranking

## Output: Ticker Audit Mode

Use:

`[COMPANY] ([TICKER]) | CANSLIM Audit`

| Dimension | Verdict | Evidence | Confidence |
|-----------|---------|----------|------------|
| C: Current earnings/sales |  |  |  |
| A: Annual earnings strength |  |  |  |
| N: New product/high/catalyst |  |  |  |
| S: Supply and demand |  |  |  |
| L: Leader or laggard |  |  |  |
| I: Institutional sponsorship |  |  |  |
| M: Market direction |  |  |  |
| Chart setup |  |  |  |
| Sell-rule risk |  |  |  |

End with:

- `Candidate tier: A/B/C/Reject/Undetermined`
- `What would improve the setup`
- `What would invalidate the setup`
- `Next research checks`

## Finviz Helper

Run the bundled helper from this skill's folder, or resolve its path from that folder, to create a repeatable Finviz starting screen:

```bash
python3 scripts/finviz_canslim_url.py --mode strict
python3 scripts/finviz_canslim_url.py --mode balanced
python3 scripts/finviz_canslim_url.py --mode early
```

The helper only prints URLs. It does not scrape, retrieve results, authenticate, or place trades. Its filters are approximate discovery presets. Confirm the filter labels and definitions in Finviz because the service may change. Validate every candidate with current source data; do not assume the screen proves chart quality, sponsorship, or market direction.

Return research in the conversation unless the user requests another destination.

## Reference

Read `references/canslim-framework.md` when you need the scoring rubric, thresholds, and execution rules.
