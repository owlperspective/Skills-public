# CANSLIM Framework

Use this as a practical O'Neil-style screen and audit rubric. It is a research workflow, not a mechanical buy signal.

## Scorecard

This 0-14 score and its tiers are this skill's custom rubric. They are not official ratings, return forecasts, or evidence of a profitable strategy.

Score an assessable dimension as `2` for strong evidence, `1` for partial evidence, or `0` for demonstrated weakness. Use `N/A` when evidence is unavailable or stale. A missing input is not a failing company characteristic. If any letter is `N/A`, show the observed subtotal with coverage, such as `5/6 observed points; 3/7 letters assessed`, and leave the total and final tier `Undetermined`. Do not treat unknowns as zero or rescale the subtotal to 14.

| Letter | Dimension | Strong Evidence | Partial Evidence | Weak / Fail |
|--------|-----------|-----------------|------------------|-------------|
| C | Current quarterly earnings and sales | EPS growth >= 25% YoY, sales growth >= 25% YoY, preferably accelerating | one of EPS/sales strong, or growth positive but decelerating | weak or negative growth |
| A | Annual earnings strength | annual EPS growth >= 25% or strong multi-year CAGR, ROE >= 17%, strong/expanding margins | annual trend positive but less consistent | losses, declining annual EPS, weak ROE/margins |
| N | New | new product, service, management, market, industry cycle, or new high supported by fundamentals | plausible catalyst but not yet proven | no identifiable new catalyst |
| S | Supply and demand | constructive volume, volume dry-up in base/handle, breakout volume +40-50%, manageable float | mixed volume or average liquidity | heavy distribution, weak liquidity, excessive dilution |
| L | Leader or laggard | RS line strong/new high, price outperforming SPY/QQQ and industry peers | moderate leadership | lagging benchmark or peers |
| I | Institutional sponsorship | increasing high-quality fund ownership, credible sponsorship without overcrowding | sponsorship present but trend unclear | evidence of weak sponsorship or distribution |
| M | Market direction | confirmed uptrend or constructive follow-through context | mixed market / pressure | correction or a demonstrated downtrend |

Total score when all seven letters are assessable:

- `12-14`: A candidate
- `9-11`: B candidate
- `6-8`: C/watch only
- `< 6`: reject

For current quarterly earnings, compare the same fiscal quarter year over year on a consistent EPS basis. A 25% sequential increase does not establish 25% year-over-year growth. If prior-period EPS is zero or negative, describe the transition without assigning a misleading growth percentage.

## Technical Patterns

Look for:

- Cup with handle
- Double bottom
- Flat base
- High tight flag
- Tight weekly closes
- Volume dry-up in the handle or base
- Breakout through pivot on volume at least 40-50% above average

Warnings:

- Extended far above pivot
- Late-stage base
- Wide and loose weekly action
- Repeated high-volume down weeks
- Close below the 10-week moving average on heavy volume
- Climax-style vertical run after a long advance

## Market Timing

Market context matters. Most strong bases form during corrections, but buying power usually improves only after a constructive market turn or follow-through context.

For a practical market check:

- Review SPY, QQQ, and Nasdaq/S&P index trend.
- Check whether indexes are above key moving averages.
- Check accumulation/distribution days.
- If current evidence shows correction or pressure, downgrade long candidates by at least one tier unless the user explicitly wants early watchlist ideas. State the unadjusted score and the market adjustment separately; the score and adjusted tier can differ. Missing market history means `M: N/A`, with the final tier undetermined.

## Execution Rules

Always include these as risk discipline, not personal advice:

- Cut losses quickly if a position falls about 7-8% below the purchase price.
- If a stock gains 20% within the first 3 weeks after breakout, flag the 8-week hold rule as potentially relevant.
- Normal profit-taking zone is often 20-25% unless the stock behaves like a power leader.
- Watch for climax tops, major reversals, and high-volume closes below the 10-week moving average.

## Suggested Initial Finviz Filters

Balanced starting point:

- EPS growth this fiscal year: over 25%, checking whether the source field is an estimate
- EPS growth past 5 years: over 15%
- Quarterly EPS growth versus the same quarter a year earlier: over 25%
- Quarterly sales growth versus the same quarter a year earlier: over 25%
- ROE: over 15%
- Operating margin: positive

Stricter starting point:

- EPS growth and sales growth both over 25%
- ROE over 20%
- Price above 50-day and 200-day moving averages
- Relative volume or volume strength improving
- Market cap and average volume high enough for liquidity

The Finviz filter is only a first pass. CANSLIM requires validation of chart structure, market direction, sponsorship, and quality of the earnings move.


## Finviz field definitions

Finviz labels its quarterly fields as qtr over qtr, but defines them as comparisons with the same quarter a year earlier. Its current-fiscal-year EPS growth field is an estimate. Keep estimates separate from reported results. See [Finviz's screener documentation](https://finviz.com/help/screener).
