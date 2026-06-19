import difflib
import re
import shutil
import tempfile
from pathlib import Path
from typing import Annotated

import typer
from bake import command, console
from bakelib import GitHubActionsTools, PythonLibSpace
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

problem_option = Annotated[str | None, typer.Option("-p", "--problem")]
force_option = Annotated[bool, typer.Option("-f", "--force")]


class MyBakebook(GitHubActionsTools, PythonLibSpace):
    ci: bool = False
    problem: str = "copy_list_with_random_pointer"

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

    def _convert_notebooks_to_python(self, base_dir: Path = Path("leetcode")) -> None:
        self.ctx.run(f"uv run jupytext --to py:percent {base_dir}/**/*.ipynb")
        for notebook in base_dir.rglob("*.ipynb"):
            notebook.unlink()

    @command("nb-to-py", help="Convert all .ipynb to .py and delete .ipynb")
    def notebook_to_python(self):
        console.echo("Converting all .ipynb files in leetcode/ to .py files...")
        self._convert_notebooks_to_python()
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

    # leetcode/ is generated from JSON templates via `lcpy gen --all`:
    #   src/leetcode_py/cli/resources/leetcode/json/problems/*.json (source of truth)
    #   + src/.../leetcode/{{cookiecutter.problem_name}}/ (cookiecutter template)
    #   → leetcode/<problem_name>/{solution.py, test_solution.py, helpers.py, ...}
    #
    # To fix drift: edit the JSON file in src/.../json/problems/, NOT the generated file.
    @command("check-consistency", help="Check leetcode/ consistency with JSON source of truth")
    def check_consistency(
        self,
        backup_dir: Annotated[
            str | None,
            typer.Option("-b", "--backup", help="Path to backup directory (auto if omitted)"),
        ] = None,
    ):
        leetcode_path = Path("leetcode")

        if not leetcode_path.exists():
            console.error("leetcode/ directory not found")
            raise typer.Exit(1)

        auto_mode = backup_dir is None
        if auto_mode:
            with tempfile.TemporaryDirectory() as tmp:
                backup_path = Path(tmp) / "leetcode"
                console.echo("Auto-backing up leetcode/...")
                shutil.copytree(leetcode_path, backup_path)
                console.echo("Deleting leetcode/...")
                shutil.rmtree(leetcode_path)
                console.echo("Regenerating all problems...")
                self.ctx.run("uv run lcpy gen --all -o leetcode --force")
                console.echo("Converting notebooks to .py...")
                self._convert_notebooks_to_python(leetcode_path)
                console.echo("Linting generated files...")
                self.lint()
                try:
                    self._run_consistency_check(leetcode_path, backup_path)
                finally:
                    console.echo("Restoring original leetcode/...")
                    shutil.rmtree(leetcode_path)
                    shutil.copytree(backup_path, leetcode_path)
        else:
            backup_path = Path(backup_dir)
            if not backup_path.exists():
                console.error(f"Backup directory not found: {backup_dir}")
                raise typer.Exit(1)
            self._run_consistency_check(leetcode_path, backup_path)

    def _run_consistency_check(self, leetcode_path: Path, backup_path: Path) -> None:
        files_to_check = [
            "README.md",
            "__init__.py",
            "helpers.py",
            "test_solution.py",
            "playground.py",
        ]
        drifted_files: list[str] = []
        drifted_problems: set[str] = set()

        for problem_dir in sorted(leetcode_path.iterdir()):
            if not problem_dir.is_dir():
                continue

            problem_name = problem_dir.name
            backup_problem = backup_path / problem_name

            if not backup_problem.exists():
                console.echo(f"  New problem (not in backup): {problem_name}")
                continue

            for filename in files_to_check:
                current_file = problem_dir / filename
                backup_file = backup_problem / filename

                if not current_file.exists() and not backup_file.exists():
                    continue

                if current_file.exists() != backup_file.exists():
                    relative = f"leetcode/{problem_name}/{filename}"
                    drifted_files.append(relative)
                    drifted_problems.add(problem_name)
                    status = "missing in backup" if backup_file.exists() else "missing in generated"
                    console.error(f"  Drift: {relative} ({status})")
                    continue

                current_text = current_file.read_text()
                backup_text = backup_file.read_text()

                if filename == "playground.py":
                    current_text = self._strip_jupytext_metadata(current_text)
                    backup_text = self._strip_jupytext_metadata(backup_text)

                if current_text != backup_text:
                    relative = f"leetcode/{problem_name}/{filename}"
                    drifted_files.append(relative)
                    drifted_problems.add(problem_name)
                    diff = difflib.unified_diff(
                        backup_text.splitlines(),
                        current_text.splitlines(),
                        fromfile=f"committed/{relative}",
                        tofile=f"generated/{relative}",
                        lineterm="",
                    )
                    diff_text = "\n".join(diff)
                    syntax = Syntax(diff_text, "diff", theme="monokai")
                    console.err.print(
                        Panel(
                            syntax,
                            title=f"[bold red]Drift:[/] {relative}",
                            border_style="red",
                            padding=(0, 1),
                        )
                    )

        if drifted_files:
            console.echo("")
            console.error(
                f"Consistency check FAILED: {len(drifted_problems)} problem(s) "
                f"have drift across {len(drifted_files)} file(s)"
            )
            fix_text = Text.from_markup(
                "[bold]Fix:[/] update JSON or generated file so they stay consistent.\n\n"
                "[dim]JSON:[/]     "
                "src/leetcode_py/cli/resources/leetcode/json/problems/<problem>.json\n"
                "[dim]Template:[/] "
                "src/leetcode_py/cli/resources/leetcode/{{cookiecutter.problem_name}}/"
            )
            console.err.print(Panel(fix_text, border_style="yellow", padding=(0, 2)))
            raise typer.Exit(1)

        console.success("Consistency check PASSED: all files match JSON source of truth")

    @staticmethod
    def _strip_jupytext_metadata(text: str) -> str:
        return re.sub(r"^# ---\n#.*?\n# ---\n", "", text, count=1, flags=re.DOTALL)


bakebook = MyBakebook()
