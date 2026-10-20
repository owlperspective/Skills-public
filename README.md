# Owl Perspective Skills

Public AI skills for practical research and learning.

## Investment Gem

[Investment Gem](investment-gem/SKILL.md) guides an AI assistant through company research, stock comparisons, and sector deep dives. It covers business economics, financial statements, earnings quality, valuation, and risks, with optional price-action context.

The skill uses public filings, company investor materials, and available market data. It requires no particular paid data provider, API key, database, or companion skill. Current research needs browsing or another reliable source of current documents and prices. Without those tools, it can analyze documents you supply and identify the limits of the evidence.

## Use it

Copy the complete `investment-gem` folder into your assistant's supported skills location. The instructions are contained in `SKILL.md`; `agents/openai.yaml` supplies optional display metadata for compatible assistants. You can also attach `SKILL.md` to a conversation and ask the assistant to follow it.

Example requests:

- "Use Investment Gem to research this company using its latest filings. Explain the business, cash generation, dilution, valuation, and main risks."
- "Use Investment Gem to compare these two stocks. Match the reporting periods and explain which metrics are actually comparable."
- "Use Investment Gem for a semiconductor sector deep dive. Explain the candidate universe, screen for cycle resilience, and investigate up to three finalists."
- "Use Investment Gem to review this uploaded annual report. Identify what can be established from the document and what still needs current evidence."

The public skill contains no personal portfolio or watchlist data, private service endpoints, database-saving workflow, custom DCF rules, or FMP integration. Research is returned in the conversation unless another output is requested.
