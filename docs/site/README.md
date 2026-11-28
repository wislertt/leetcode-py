# Docs

This directory is the [Mintlify](https://mintlify.com) site published at [leetcode-py.wisl.dev](https://leetcode-py.wisl.dev). Check broken links with `bake docs-check`.

## Agent surfaces

Mintlify serves machine-readable endpoints for AI agents automatically:

- `llms.txt` and `llms-full.txt` are auto-generated from the navigation in `docs.json`. Zero maintenance.
- `/mcp` is a search MCP server over the docs. Zero maintenance.
- `skill.md` is hand-written and served at `/skill.md`; it overrides the low-quality file Mintlify auto-generates. Do not delete it. It is served raw, so it cannot carry MDX-only components: every code example in it must be a verbatim copy of a tested source (a `.mdx` page example or a file under `leetcode/<problem>/`).
- `markdown.instructions` in `docs.json` is injected as an `Agent Instructions` block into `llms.txt`, `llms-full.txt`, and every Markdown page export.

The `lcpy` CLI help epilog advertises these endpoints (`AGENT_DOCS_EPILOG` in `src/leetcode_py/cli/main.py`), and tests in `tests/cli/test_main.py` assert they stay there.
