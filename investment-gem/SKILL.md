---
name: investment-gem
description: Use when researching a publicly traded company, comparing stocks, preparing an evidence-based investment memo, or screening a sector for further research. Covers business quality, financial statements, earnings quality, valuation, risks, and optional price-action context.
---

# Investment Gem

Produce equity research that explains how a business makes money, whether its financial results support the story, and what its current price assumes. Keep reported facts, management guidance, third-party estimates, and analytical inference distinct.

This skill is self-contained. Use available browsing, document-reading, and calculation tools; no particular data provider, paid service, account, or other skill is required. If current research tools are unavailable, analyze supplied documents and clearly date the result. Do not present historical evidence as a current investment assessment.

## Choose the scope

- **Company report:** Analyze one company. Default to a concise memo of roughly 1,000 to 1,500 words, adjusting to the question and available evidence.
- **Comparison:** Compare a few named companies on matched periods and economically comparable metrics. Explain differences that prevent a clean ranking.
- **Sector deep dive:** Build a documented research universe, screen it with sector-appropriate criteria, and investigate up to three supported finalists. Report fewer when the evidence does not justify three.
- **Focused question:** Answer the requested issue directly. Do not generate a full report for a question about one earnings release or accounting concern.

Resolve ambiguous tickers, share classes, exchanges, and company names before retrieving company-specific data. If identity cannot be established, restrict conclusions to the supplied material and state that limitation. Establish the reporting currency, fiscal year-end, business model, and research date where possible. Use the user's stated horizon and constraints; otherwise explain the horizon assumed for the analysis without inventing portfolio holdings, risk tolerance, or personal suitability.

## Establish the evidence

### Source selection

For a full report, seek the latest annual filing, any newer interim filing, the latest earnings release, and relevant management commentary. Use a shareholder letter, company-hosted transcript, prepared remarks, or investor presentation where available. For non-US issuers, use the relevant regulator, exchange, and local filing equivalents.

Resolve reported financial facts primarily from regulatory filings and their notes, then company releases and presentations, then management commentary. Use reputable market-data sources for quotes and price history. Treat third-party summaries as leads and cross-check thesis-critical figures against original documents. Management commentary is evidence of management's view, not independent confirmation.

- Prefer direct regulator and investor-relations sources. Follow document links rather than treating search snippets as sufficient evidence.
- Use any available structured data as a convenience, checking its period, units, currency, and definitions. No connector is a prerequisite.
- Retrieve changing facts when the task calls for current analysis. Label a delayed quote, prior close, or historical valuation explicitly.
- Record publication date and financial period separately. State the quote's date, time, timezone, trading session, and source when available. Never invent a timestamp the source does not provide.
- Distinguish company guidance, dated analyst consensus, and your own forecasts. Never imply consensus exists when it cannot be sourced.
- Resolve material discrepancies rather than averaging conflicting values. Explain the treatment and its effect on the conclusion.
- When access is blocked or a metric is not disclosed, state what is missing and continue with supported analysis. Missing evidence is not adverse evidence or evidence that a risk is absent.

Build a source ledger as you research. Cite material figures, claims, and catalysts near their use. Include document links and periods in the final report. Once the required evidence is covered, stop broad collection unless a material conflict or thesis question remains unresolved.

### Comparable financial history

Where disclosed, collect three annual periods and the latest comparable interim periods. Show only the history needed to assess the business. Keep reported, trailing-twelve-month, and forecast data in separate columns.

Prioritize revenue, operating profit and margin, net income, operating cash flow, capital expenditure, cash, debt, diluted shares, and sector KPIs. Reconcile acquisitions, disposals, currency effects, restatements, changes in segment definitions, and non-GAAP adjustments when material. Do not fill a template with unsupported estimates.

## Analyze the business

Explain the customer, product, revenue model, cost structure, and reinvestment needs. Identify the drivers that actually move revenue and profit, such as volume, pricing, usage, retention, utilization, or mix. Distinguish organic growth from acquisitions and cyclical recovery.

Assess competitive advantage through demonstrated economics. Relevant evidence can include pricing power, retention, switching costs, network effects, differentiated technology, distribution, brand preference, or structural cost advantages. Explain how the advantage protects earning power, whether it is strengthening or eroding, and what would challenge it. A large market or popular product alone does not establish a moat.

Check management's capital allocation through per-share outcomes, investment returns, acquisitions, repurchases, incentives, and the consistency of guidance. Separate announced opportunities from demonstrated adoption and commercial results. An unproven adjacent market belongs in an explicitly uncertain scenario, rather than automatically in the central forecast.

### Select metrics by business model

Use the following as a menu. Choose a few relevant indicators, define unfamiliar terms, and avoid metrics the company does not disclose reliably.

| Business model | Useful operating evidence | Valuation context and cautions |
|---|---|---|
| Subscription or usage-based software | Retention, customer growth, usage, remaining obligations, gross margin, dilution | Revenue and cash-flow multiples with growth, margins, and compensation context. Define the margin used in any Rule of 40 calculation. |
| Marketplace or transaction platform | Transaction volume, take rate, active customers, frequency, contribution margin | Distinguish gross merchandise value from revenue and gross from net revenue recognition. |
| Advertising, media, or gaming | Users, engagement, revenue per user, bookings, churn, content investment | Account for content and development capitalization and platform exposure. |
| Retail, consumer, or restaurants | Comparable sales, traffic versus ticket, inventory, unit economics, franchise mix | Separate price increases and new locations from healthy underlying demand. |
| Semiconductors or hardware | End-market demand, inventory, utilization, margins, backlog quality | Separate subsectors and normalize the cycle; peak earnings can make a multiple look cheap. |
| Industrials or aerospace | Orders, backlog conversion, book-to-bill, segment margins, working capital | Distinguish short-cycle demand, long contracts, customer advances, and fixed-price risk. |
| Banks | Deposit funding, net interest margin, credit quality, capital adequacy, return on tangible equity | Prefer equity, tangible-book, and earnings measures. Generic enterprise-value and free-cash-flow analysis usually misrepresents bank economics. |
| Insurers or asset managers | Underwriting results and reserves, or assets under management and net flows | Match metrics to the model. Insurance, banking, and asset management are not interchangeable peers. |
| REITs or real estate | Occupancy, leasing spreads, same-property income, recurring maintenance, debt maturities | Use FFO/AFFO, asset values, and cash coverage where appropriate; reconcile company definitions. |
| Energy or materials | Volumes, realized prices, unit costs, sustaining investment, reserves, decline rates | Use cycle-aware cash flow and asset economics, with explicit commodity assumptions. |
| Utilities or infrastructure | Rate base, allowed returns, regulatory recovery, capital plan, funding needs | Distinguish recoverable investment from discretionary growth and assess financing capacity. |
| Telecom or connectivity | Subscribers, churn, pricing, network investment, leverage | Include recurring capital intensity, spectrum commitments, and lease treatment. |
| Healthcare or profitable pharma | Procedure or product demand, reimbursement, margins, patent exposure | Separate devices, services, diagnostics, and commercial drug economics. |
| Pre-profit biotech or early-stage businesses | Cash runway, funding needs, milestones, trial endpoints, unit economics where established | Avoid earnings multiples. Disclose the evidence behind any event probabilities or pipeline values. |

For mixed businesses, analyze material segments separately when their economics differ. Explain the weights and limits of any combined assessment.

## Test financial and earnings quality

Read the cash-flow statement and relevant notes alongside the income statement. Ask whether growth turns into cash and whether that cash accrues to each share.

- Compare earnings with operating cash flow over several periods. Explain receivables, inventory, deferred revenue, customer advances, factoring, and supplier-payment timing before treating conversion as strong or weak.
- Reconcile reported and adjusted profit. Recurring restructuring, acquisition, litigation, or compensation costs do not become irrelevant because management excludes them.
- Look for deteriorating retention, orders, traffic, utilization, or credit metrics that headline revenue may conceal. A slower growth rate differs from an absolute decline.
- Compare dilution with repurchases. A buyback announcement does not prove the share count fell or that value was created.
- Assess unrestricted liquidity, refinancing needs, covenants, interest coverage, leases, pension obligations, and other material claims. Restricted or operationally necessary cash may not be freely distributable.
- Check concentration, related parties, auditor concerns, restatements, internal controls, and changing disclosure definitions when relevant.

### Calculation conventions

Use a calculator or executable calculation tool for nontrivial arithmetic. Show definitions and material adjustments so a reader can reproduce the result.

| Measure | Convention |
|---|---|
| Revenue growth | Compare like periods and definitions. Separate organic and currency effects when disclosed. |
| Margin | Name the profit measure and divide by matched-period revenue. Report margin changes in percentage points. |
| Simple free cash flow | Operating cash flow less capital expenditure, treating capex as a positive outflow in this formula. Identify recurring capitalized software, content, or other investment needed to sustain operations. |
| Cash conversion | State whether the denominator is net income or another profit measure. A negative or near-zero denominator can make the ratio uninformative. |
| Stock-based compensation | Disclose it relative to revenue and cash flow. If showing cash flow after a compensation adjustment, reconcile it and label it as analytical. Avoid charging the same awards again through dilution or offsetting repurchases in a valuation. |
| Per-share history | Use period-matched diluted weighted-average shares for historical per-share earnings and cash flow. Keep current ownership claims separate. |
| Equity and enterprise value | Match price, share count, share class, currency, and date. Reconcile debt, cash, and other material claims for enterprise value. Do not divide enterprise value by an equity-only cash-flow measure. |
| Returns on capital | Disclose tax and invested-capital definitions, generally using average capital. Use sector equivalents where ordinary ROIC is inappropriate. |
| Operating accruals | If useful, calculate net income less operating cash flow, divided by average total assets. Explain working-capital effects before interpreting the result. |

When earnings or cash flow cross zero, show the absolute change and explain the transition rather than presenting a misleading growth percentage or compound growth rate. Do not compare a fiscal-year multiple with a calendar-year estimate without explaining the mismatch.

## Evaluate valuation without false precision

Separate business quality from the price paid. A good company can be expensive, and a low multiple can reflect a deteriorating business.

Choose valuation methods that fit the business and the available evidence. Relative multiples, normalized earnings or cash flow, asset values, and sector-specific approaches may be useful. There is no mandatory valuation model, preset discount rate, fixed growth path, or proprietary scoring formula in this skill.

1. Select roughly three to five relevant peers when evidence supports them. Explain differences in business mix, growth, margins, leverage, geography, accounting, and fiscal periods. Use fewer peers when the alternatives are misleading.
2. Match the numerator and denominator. Distinguish equity multiples from enterprise multiples, historical from forward measures, and reported from adjusted results. Do not call a small peer sample a sector average.
3. Explain why a premium or discount might be justified. Peer multiples describe market pricing and do not independently establish fair value.
4. If making forecasts, show the operational assumptions, their evidence, and the period. Separate management guidance from your own assumptions. Use downside, central, and upside scenarios when they clarify material uncertainty; omit numerical outputs that cannot be supported.
5. If estimating value, disclose the method, valuation date, share basis, and sensitivity to the inputs that matter most. Distinguish a future scenario price from value today. Do not average incompatible methods or select the method solely because it produces the highest estimate.
6. Without a reliable current quote or defensible valuation inputs, leave current attractiveness undetermined. You can still assess business quality and identify the evidence needed for a valuation.

Use qualitative assessments by default. If the user requests numerical scores, define a transparent, task-appropriate rubric and disclose missing inputs. Do not invent neutral scores or quietly redistribute missing weights. Keep business quality, valuation, and price action visible as distinct judgments rather than hiding them in a single rating.

## Add price-action context only when useful

Use price and volume analysis when requested or when it materially helps the question. A weak chart alone does not establish weak business economics, and a strong chart does not prove attractive value.

Use sufficient daily history for the calculation and a clearly identified benchmark. State whether prices reflect splits and dividends. Use the latest completed trading day for daily indicators; distinguish it from any intraday header quote.

- A 50-day or 200-day simple moving average needs at least that many daily observations. Claims that an average is rising or falling need additional history.
- For relative strength, compare company and benchmark returns over the same dates and adjustment basis. State the return window; do not confuse relative performance with the RSI indicator.
- Describe volume patterns or support and resistance only when the data supports them. Price-only data cannot establish accumulation, distribution, or order flow.
- Report unavailable history as a market-data gap. Do not infer moving averages, short interest, or institutional ownership from company filings or a chart image alone.

Keep market timing separate from the fundamental conclusion. A large drawdown can coexist with improving value, deteriorating fundamentals, or both; identify which the evidence supports.

## Sector deep-dive workflow

Define the sector, geography, size or liquidity constraints, research date, and comparison universe. If the user supplied no constraints, state practical assumptions. Describe how candidates were found and any coverage limits; do not imply an exhaustive market scan from a few search results.

Screen with sector-relevant evidence of durable economics, cash generation, financial resilience, growth quality, and manageable risks. Use thresholds only when justified for that sector or specified by the user. A fixed ROIC hurdle, positive conventional free cash flow, or software growth metric is not a universal test.

Research finalists before ranking them. Compare business quality and valuation on consistent evidence, explain ranking criteria, and show price-action context separately. Keep incomplete candidates marked as such. Do not fill a quota with weakly supported names or present a research shortlist as a personalized portfolio.

## Compose the report

For a full company report, use this adaptable structure. Merge short sections where it improves readability; preserve the substantive checks.

1. **Header and evidence status.** Company, ticker and exchange, research date, business model, reporting currency and units, quote source and timestamp. Put material gaps or source conflicts and their implications near the top.
2. **Investment view.** State the central judgment, strongest supporting evidence, and the uncertainty most likely to change it. Distinguish business quality, price attractiveness, and optional market timing.
3. **Business and competitive position.** Explain the drivers, relevant segment economics, competitive protection, and management's capital allocation.
4. **Financial evidence.** Show a compact matched-period table of the relevant financials and sector KPIs. Discuss trends, cash conversion, dilution, and balance-sheet resilience.
5. **Valuation and peers.** Present supported comparisons and any explicit scenario assumptions. Explain what the price appears to require and what remains unproven.
6. **Catalysts, risks, and disconfirming evidence.** Name observable events or measurements, expected timing where sourced, the mechanism affecting the thesis, and evidence that would invalidate it. Separate the same underlying risk from its repeated symptoms.
7. **What to monitor.** Identify the next filing, operating metric, milestone, or price assumption that would materially update the view. Use sourced dates or label timing as unknown.
8. **Sources and limitations.** List the material documents, publication dates, financial periods, links, and their use. Identify unresolved gaps without repeating the whole report.

Write in short paragraphs with compact tables where they make comparisons easier. Define necessary financial terms, avoid promotional claims, and give uncertainty an economic meaning. A report can be inconclusive when the evidence does not support a firm judgment.

### Example request

> Use Investment Gem to compare two listed software companies using their latest filings and current quotes. Focus on retention, cash conversion, dilution, balance-sheet risk, and valuation. Explain where the evidence is incomplete.

Adapt the same workflow to a bank by changing the operating and valuation metrics, rather than forcing a software template onto it.

## Delivery and final checks

Return the analysis in the conversation unless the user requests a file or another destination. For a requested file, use the chosen location and preserve existing work. An external save requires an available integration and the user's instruction; do not assume a research database exists or claim a save without confirmation from the tool.

Before delivering, verify that the report:

- Identifies the correct security, research date, quote basis, and financial periods.
- Uses sector-appropriate metrics with consistent currency, units, accounting definitions, and share bases.
- Reconciles material numerical claims to sources and distinguishes estimates from facts.
- Gives substantive adverse evidence and missing evidence their different meanings.
- Keeps current valuation claims within the support of the available quote and assumptions.
- Explains the business, the price, the principal risk, and what would change the conclusion.
- Includes citations, source gaps, and an accurate statement of any requested file or save status.
