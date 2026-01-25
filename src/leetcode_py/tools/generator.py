import json
import subprocess
from pathlib import Path

import typer
from cookiecutter.main import cookiecutter
from ruff.__main__ import find_ruff_bin
from ty.__main__ import find_ty_bin

from leetcode_py.cli.utils.problem_finder import get_tags_for_problem


def load_json_data(json_path: Path) -> dict:
    if not json_path.exists():
        typer.echo(f"Error: {json_path} not found", err=True)
        raise typer.Exit(1)

    try:
        with open(json_path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        typer.echo(f"Error reading {json_path}: {e}", err=True)
        raise typer.Exit(1) from None


def check_problem_exists(problem_name: str, output_dir: Path, force: bool) -> None:
    if not force:
        problem_dir = output_dir / problem_name
        if problem_dir.exists():
            typer.echo(
                f"Error: Problem '{problem_name}' already exists. Use --force to overwrite.",
                err=True,
            )
            raise typer.Exit(1)


def batch_format_and_check(directories: list[Path]) -> None:
    if not directories:
        return

    # Filter to only existing directories
    existing_dirs = [d for d in directories if d.exists()]
    if not existing_dirs:
        return

    ruff_bin = find_ruff_bin()
    ty_bin = find_ty_bin()

    # Convert paths to strings for subprocess
    dir_paths = [str(d) for d in existing_dirs]

    # Ruff rules to enforce (same as pyproject.toml)
    ruff_rules = "ARG,B,C4,E,F,I,N,PGH,PIE,PYI,RUF,SIM,UP"

    # 1. ruff format (all directories in one call)
    subprocess.run(
        [ruff_bin, "format", "--exit-non-zero-on-format", *dir_paths],
        check=False,
    )

    # 2. ruff check --fix (ignore ARG002 in solution.py, B018 in playground files)
    subprocess.run(
        [
            ruff_bin,
            "check",
            "--select",
            ruff_rules,
            "--per-file-ignores",
            "**/solution.py:ARG002",
            "--per-file-ignores",
            "**/playground.ipynb:B018",
            "--fix",
            "--exit-non-zero-on-fix",
            *dir_paths,
        ],
        check=False,
    )

    # 3. ty check (ignore unresolved-import in playground files, ARG002 in solution files)
    subprocess.run(
        [
            ty_bin,
            "check",
            "--error-on-warning",
            "--no-progress",
            "--exclude",
            "**/playground.ipynb",
            *dir_paths,
        ],
        check=False,
    )


def merge_tags(data: dict) -> dict:
    """Merge tags from get_tags_for_problem with existing JSON tags."""
    problem_name = data.get("problem_name", "")
    if not problem_name:
        return data

    # Get tags from tag system
    system_tags = get_tags_for_problem(problem_name)

    # Get existing tags from JSON
    existing_tags = data.get("_tags", {}).get("list", [])

    # Merge and deduplicate tags
    all_tags = list(set(system_tags + existing_tags))

    # Update data with merged tags
    if all_tags:
        data["_tags"] = {"list": all_tags}

    return data


def generate_from_template(data: dict, template_dir: Path, output_dir: Path) -> None:
    """Generate problem files using cookiecutter template."""
    try:
        # Merge tags before generating
        data = merge_tags(data)

        cookiecutter(
            str(template_dir),
            extra_context=data,
            no_input=True,
            overwrite_if_exists=True,
            output_dir=str(output_dir),
        )
        problem_name = data.get("problem_name", "unknown")
        typer.echo(f"✅ Generated problem: {problem_name}")
    except Exception as e:
        typer.echo(f"Error generating template: {e}", err=True)
        raise typer.Exit(1) from None


def generate_problem(
    json_path: Path, template_dir: Path, output_dir: Path, force: bool = False
) -> None:
    data = load_json_data(json_path)
    problem_name = data.get("problem_name", "unknown")
    check_problem_exists(problem_name, output_dir, force)
    generate_from_template(data, template_dir, output_dir)
