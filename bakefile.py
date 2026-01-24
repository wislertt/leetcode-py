from bake import Context, console
from bakelib import PythonSpace


class MyBakebook(PythonSpace):
    def lint(self, ctx: Context) -> None:
        ctx.run("uv run python scripts/sort_tags.py")
        ctx.run("uv run python scripts/check_tag_problems.py")
        super().lint(ctx)

    def test(self, ctx: Context) -> None:
        tests_path = "tests/ leetcode/"
        self._test(ctx, tests_path=tests_path)


bakebook = MyBakebook()


@bakebook.command()
def hello(name: str = "world"):
    console.echo(f"Hello {name}!")
