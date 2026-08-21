from importlib.metadata import version

import typer

from .commands.gen import generate
from .commands.list import list_problems
from .commands.scrape import scrape

DOCS_URL = "https://leetcode-py.wisl.dev"
_INSTALL_SKILL_CMD = f"npx skills add {DOCS_URL}"
AGENT_DOCS_EPILOG = f"""Docs: {DOCS_URL}
Full docs in one file (for AI agents): {DOCS_URL}/llms-full.txt
Docs index: {DOCS_URL}/llms.txt
Agent skill: {DOCS_URL}/skill.md
Install agent skill: `{_INSTALL_SKILL_CMD}`
Docs search via MCP: {DOCS_URL}/mcp"""

app = typer.Typer(
    help="LeetCode problem generator - Generate and list LeetCode problems",
    epilog=AGENT_DOCS_EPILOG,
)


def show_version():
    typer.echo(f"lcpy version {version('leetcode-py-sdk')}")
    raise typer.Exit()


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-V", help="Show version and exit"),
):
    if version:
        show_version()

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


app.command(name="gen")(generate)
app.command(name="scrape")(scrape)
app.command(name="list")(list_problems)
