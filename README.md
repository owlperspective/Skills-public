# Owl Perspective Skills

Public AI skills for practical research and learning.

## Investment Gem

[Investment Gem](investment-gem/SKILL.md) guides an AI assistant through company research, stock comparisons, and sector deep dives. It covers business economics, financial statements, earnings quality, valuation, and risks, with optional price-action context.

The skill uses public filings, company investor materials, and available market data. It requires no particular paid data provider, API key, database, or companion skill. Current research needs browsing or another reliable source of current documents and prices. Without those tools, it can analyze documents you supply and identify the limits of the evidence.

## Keep Agent Awake

[Keep Agent Awake](keep-agent-awake/SKILL.md) prevents idle sleep during an active local task and releases its owned request when work finishes. The helper supports macOS through caffeinate, native Windows through its execution-state API, and Linux through systemd-inhibit with an accessible systemd-logind service.

It requires Python 3.9 or newer, with no pip packages. The display can sleep by default; keeping it awake is optional on macOS and Windows. The helper supports timeouts and cancellation and changes no persistent power settings. It cannot extend AI usage limits or keep a client laptop awake from a remote executor. See the skill for commands, platform limits, and cleanup.

## Use it

Copy a complete skill folder into your assistant's supported skills location, or use a symlink where supported. Each skill starts at `SKILL.md`; `agents/openai.yaml` supplies optional display metadata for compatible assistants. Preserve any scripts or other resources in the folder. For conversation-only use, Investment Gem's `SKILL.md` is self-contained. Keep Agent Awake needs its helper on the computer where it will run. Check the host's current documentation for installation and invocation details.

Example requests:

- "Use Investment Gem to research this company using its latest filings. Explain the business, cash generation, dilution, valuation, and main risks."
- "Use Investment Gem to compare these two stocks. Match the reporting periods and explain which metrics are actually comparable."
- "Use Investment Gem for a semiconductor sector deep dive. Explain the candidate universe, screen for cycle resilience, and investigate up to three finalists."
- "Use Investment Gem to review this uploaded annual report. Identify what can be established from the document and what still needs current evidence."
- "Use Keep Agent Awake during this long local task, allow the display to sleep, and release the request when finished."

Investment Gem contains no personal portfolio or watchlist data, private service endpoints, database-saving workflow, custom DCF rules, or FMP integration. Research is returned in the conversation unless another output is requested.
