# Owl Perspective Skills

Public AI skills for practical research and learning.

## Investment Gem

[Investment Gem](investment-gem/SKILL.md) guides an AI assistant through company research, stock comparisons, and sector deep dives. It covers business economics, financial statements, earnings quality, valuation, and risks, with optional price-action context.

The skill uses public filings, company investor materials, and available market data. It requires no particular paid data provider, API key, database, or companion skill. Current research needs browsing or another reliable source of current documents and prices. Without those tools, it can analyze documents you supply and identify the limits of the evidence.

## Keep Agent Awake

[Keep Agent Awake](keep-agent-awake/SKILL.md) prevents idle sleep during an active local task and releases its owned request when work finishes. The helper supports macOS through caffeinate, native Windows through its execution-state API, and Linux through systemd-inhibit with an accessible systemd-logind service.

It requires Python 3.9 or newer, with no pip packages. The display can sleep by default; keeping it awake is optional on macOS and Windows. The helper supports timeouts and cancellation and changes no persistent power settings. It cannot extend AI usage limits or keep a client laptop awake from a remote executor. See the skill for commands, platform limits, and cleanup.

## Installation

Clone once, or use your existing clone:

```sh
git clone https://github.com/owlperspective/Skills-public.git "$HOME/Projects/Skills-public"
```

Install both complete skill folders in your agent's user-level skills directory:

| Agent | Skills directory | Invoke in agent chat |
|---|---|---|
| [Codex CLI / IDE](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/` | `$investment-gem` or `$keep-agent-awake` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `/investment-gem` or `/keep-agent-awake` |
| [Cursor](https://cursor.com/docs/skills) | `~/.cursor/skills/` | Type `/` and select either skill. |

On macOS/Linux, use symlinks for Codex or Claude Code to keep one maintained copy. Set the paths for your clone and agent; existing destinations, including broken links, are left untouched.

```sh
skills_repo="$HOME/Projects/Skills-public"
skills_dir="$HOME/.agents/skills" # Claude Code: "$HOME/.claude/skills"
mkdir -p "$skills_dir"
for skill in investment-gem keep-agent-awake; do
  skill_target="$skills_dir/$skill"
  if [ ! -f "$skills_repo/$skill/SKILL.md" ]; then
    printf 'Missing source: %s\n' "$skills_repo/$skill"
  elif [ -e "$skill_target" ] || [ -L "$skill_target" ]; then
    printf 'Keeping existing: %s\n' "$skill_target"
  else
    ln -s "$skills_repo/$skill" "$skill_target"
  fi
done
```

On Windows, copy both complete folders into the listed directory under your user profile. Open a new agent session if the skills do not appear. Keep the clone in place when using symlinks; source updates also update the linked installation.

## Usage

Add the appropriate invocation from the table to your request, for example:

- **Investment Gem:** "Research Microsoft using current filings and quotes. Explain business quality, cash generation, valuation, and risks."
- **Keep Agent Awake:** "Keep this computer awake during the task, allow the display to sleep, and release the request when finished."

For other agents, follow their skills documentation or ask them to read the chosen `SKILL.md`. Investment Gem can also be attached directly to a conversation. Keep Agent Awake requires its Python helper and local command execution on the computer to protect; attaching its instructions alone does not prevent sleep.

Investment Gem contains no personal portfolio or watchlist data, private service endpoints, database-saving workflow, custom DCF rules, or FMP integration. Research is returned in the conversation unless another output is requested.
