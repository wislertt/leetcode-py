import shutil
from pathlib import Path
from typing import Annotated

import typer
from bake import command, console
from bakelib import GitHubActionsTools, PythonLibSpace

problem_option = Annotated[str | None, typer.Option("-p", "--problem")]
force_option = Annotated[bool, typer.Option("-f", "--force")]


class MyBakebook(GitHubActionsTools, PythonLibSpace):
    ci: bool = False
    problem: str = "path_sum_iii"

    def lint(self) -> None:
        self.ctx.run("uv run python scripts/sort_tags.py")
        self.ctx.run("uv run python scripts/check_tag_problems.py")
        super().lint()

    def test(self) -> None:
        tests_paths: list[str] = ["tests/", "leetcode/"]
        self._test(tests_paths=tests_paths)

    def is_problem_exist(self, problem: str) -> Path:
        problem_path = Path(f"leetcode/{problem}")
        if not problem_path.is_dir():
            console.error(f"Problem '{problem}' not found in leetcode/ directory")
            raise typer.Exit(1)

        return problem_path

    @command("p-test", help="Run problem specific tests")
    def problem_test(self, problem: problem_option = None):
        problem = problem or self.problem
        problem_path = self.is_problem_exist(problem)
        tests_path = str(problem_path / "test_solution.py")
        self._test(tests_paths=tests_path, verbose=True, coverage_report=False)

    @command("p-gen", help="Generate specific problem")
    def problem_gen(self, problem: problem_option = None, force: force_option = False):
        problem = problem or self.problem
        console.echo(f"Generating problem: {problem}")
        self.ctx.run(
            f"uv run lcpy gen -s {problem} -o leetcode {'--force' if force else ''}".strip()
        )

    @command("p-del", help="Delete specific problem directory")
    def problem_delete(self, problem: problem_option = None):
        problem = problem or self.problem
        problem_path = self.is_problem_exist(problem)
        shutil.rmtree(problem_path)
        console.echo(f"Deleted: {problem_path}")

    @command("nb-to-py", help="Convert all .ipynb to .py and delete .ipynb")
    def notebook_to_python(self):
        console.echo("Converting all .ipynb files in leetcode/ to .py files...")

        # Find, convert, and delete all .ipynb files
        for notebook in Path("leetcode").rglob("*.ipynb"):
            self.ctx.run(f"uv run jupytext --to py:percent {notebook}")
            notebook.unlink()

        console.success("Conversion complete. All .ipynb files converted to .py and deleted.")

    @command("check-test-cases", help="Find problems with few test cases")
    def check_test_cases(
        self,
        threshold: Annotated[
            int,
            typer.Option("-t", "--threshold", help="Show problems with test cases <= threshold"),
        ] = 10,
        max: Annotated[
            str,
            typer.Option(
                "-m", "--max", help="Maximum number of results to show ('none' for no limit)"
            ),
        ] = "none",
    ):
        console.echo("Checking test case coverage...")
        self.ctx.run(
            "uv run python src/leetcode_py/tools/check_test_cases.py "
            f"--threshold={threshold} --max={max}"
        )

    @command("gen-all-problems", help="Delete all problems and regenerate from JSON templates")
    def gen_all_problems(self, force: force_option = False):
        console.echo("This will DELETE all existing problems and regenerate from JSON templates.")

        if not self.ci and not typer.confirm("Are you sure?"):
            raise typer.Exit(0)

        console.echo("Deleting existing problems...")

        if Path("leetcode").exists():
            shutil.rmtree(Path("leetcode"))

        console.echo("Generating all problems...")
        force_flag = "--force" if force else ""
        self.ctx.run(f"uv run lcpy gen --all -o leetcode {force_flag}".strip())


bakebook = MyBakebook()
