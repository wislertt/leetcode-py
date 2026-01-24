from bake import Context, console
from bakelib import PythonSpace as _PythonSpace


class PythonSpace(_PythonSpace):
    def lint(self, ctx: Context) -> None:
        # TODO: fix lint
        ctx.run("uv run python scripts/sort_tags.py")
        ctx.run("uv run python scripts/check_tag_problems.py")
        ctx.run(
            "uv run toml-sort --sort-inline-arrays --in-place "
            "--sort-first=project,dependency-groups pyproject.toml"
        )
        ctx.run("uv run ruff format --exit-non-zero-on-format .")
        # ctx.run("uv run ruff check --fix --exit-non-zero-on-fix .")
        # ctx.run("uv run ty check --error-on-warning --no-progress .")
        # ctx.run("uv run deptry .")

    def test(self, ctx: Context) -> None:
        tests_path = "tests/ leetcode/"
        self._test(ctx, tests_path=tests_path)


bakebook = PythonSpace()


@bakebook.command()
def hello(name: str = "world"):
    console.echo(f"Hello {name}!")
