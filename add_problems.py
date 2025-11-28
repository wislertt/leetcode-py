import json
import os
import re
import shutil
import subprocess
import sys
import time


def get_missing_slugs():
    with open("batch_1_slugs.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]


def transform_scraped_data(data):
    """Transforms scraped data into the format expected by cookiecutter/gen."""
    transformed = {}

    # Basic fields
    # Sanitize problem_name
    problem_name = data.get("slug", "").replace("-", "_")
    if problem_name and problem_name[0].isdigit():
        problem_name = f"_{problem_name}"
    transformed["problem_name"] = problem_name
    transformed["problem_number"] = data.get("number", "0")
    transformed["problem_title"] = data.get("title", "")
    transformed["difficulty"] = data.get("difficulty", "Medium")

    # Topics: list -> string
    topics = data.get("topics", [])
    if isinstance(topics, list):
        transformed["topics"] = ", ".join(topics)
    else:
        transformed["topics"] = str(topics)

    # Description
    transformed["readme_description"] = data.get("description", "")

    # Constraints: list -> string
    constraints = data.get("constraints", [])
    if isinstance(constraints, list):
        transformed["readme_constraints"] = "\n".join([f"- {c}" for c in constraints])
    else:
        transformed["readme_constraints"] = str(constraints)

    # Examples
    examples = data.get("examples", [])
    readme_examples = []
    for ex in examples:
        # Scraped example might be dict or string?
        # 01_matrix.json shows examples as empty list []?
        # But raw_content has them.
        # If examples is list of dicts with 'text' or 'input'/'output'
        if isinstance(ex, dict):
            content = ex.get("text", "")
            if not content:
                inp = ex.get("input", "")
                out = ex.get("output", "")
                if inp and out:
                    content = f"```\nInput: {inp}\nOutput: {out}\n```"
            if content:
                readme_examples.append({"content": content})

    transformed["_readme_examples"] = {"list": readme_examples}

    # Python Code Parsing
    python_code = data.get("python_code", "")
    solution_class_name = "Solution"
    method_name = "unknown"
    method_signature = ""
    method_body = "        pass"

    # Simple regex to find class and method
    class_match = re.search(r"class\s+(\w+):", python_code)
    if class_match:
        solution_class_name = class_match.group(1)

    # Find method def
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    method_match = re.search(r"def\s+(\w+)\s*\((.*?)\)\s*(->\s*.*?)?:", python_code)
    if method_match:
        method_name = method_match.group(1)
        params = method_match.group(2)
        return_type = method_match.group(3) or ""

        # Clean params to remove 'self'
        param_list = [p.strip() for p in params.split(",") if p.strip()]
        if param_list and param_list[0] == "self":
            param_list = param_list[1:]

        clean_params = ", ".join(param_list)

        # Construct signature
        if clean_params:
            method_signature = f"(self, {clean_params}){return_type}"
        else:
            method_signature = f"(self){return_type}"

        # Snake case method name
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", method_name)
        snake_method_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

        method_body = f"        # TODO: Implement {snake_method_name}\n        return "
        if "List" in return_type:
            method_body += "[]"
        elif "int" in return_type:
            method_body += "0"
        elif "bool" in return_type:
            method_body += "False"
        elif "str" in return_type:
            method_body += '""'
        else:
            method_body += "None"

        transformed["solution_class_name"] = solution_class_name

        transformed["_solution_methods"] = {
            "list": [{"name": snake_method_name, "signature": method_signature, "body": method_body}]
        }

        # Helpers and Tests
        transformed["helpers_run_name"] = snake_method_name

        if clean_params:
            helper_sig = f"(solution_class: type, {clean_params})"
        else:
            helper_sig = "(solution_class: type)"

        transformed["helpers_run_signature"] = helper_sig

        # Extract argument names for the call
        arg_names = [p.split(":")[0].strip() for p in param_list]
        call_args = ", ".join(arg_names)

        transformed["helpers_run_body"] = (
            f"    implementation = solution_class()\n"
            f"    return implementation.{snake_method_name}({call_args})"
        )

        transformed["helpers_assert_name"] = snake_method_name
        # Infer expected type from return type
        expected_type = return_type.replace("->", "").strip()
        transformed["helpers_assert_signature"] = (
            f"(result: {expected_type}, expected: {expected_type}) -> bool"
        )
        transformed["helpers_assert_body"] = "    assert result == expected\n    return True"

        transformed["test_class_name"] = "".join(
            [word.capitalize() for word in transformed["problem_name"].split("_")]
        )
        transformed["test_class_content"] = (
            "    def setup_method(self):\n        self.solution = Solution()"
        )

        # Test Cases
        formatted_test_cases = []
        raw_test_cases = data.get("test_cases", [])

        # Count args
        arg_count = len(arg_names)

        for tc in raw_test_cases:
            # Expected length is arg_count + 1 (for expected output)
            if len(tc) == arg_count + 1:
                args = ", ".join(tc[:-1])
                expected = tc[-1]
                formatted_test_cases.append(f"({args}, {expected})")
            else:
                print(
                    f"[{data.get('slug')}] Warning: Skipping invalid test case "
                    f"(len={len(tc)}, expected={arg_count+1}): {tc}"
                )

        # Parametrize string
        if call_args:
            parametrize_str = f"{call_args}, expected"
        else:
            parametrize_str = "expected"

        # Test signature
        if clean_params:
            test_sig = f"(self, {clean_params}, expected: {expected_type})"
        else:
            test_sig = f"(self, expected: {expected_type})"

        transformed["_test_methods"] = {
            "list": [
                {
                    "name": f"test_{snake_method_name}",
                    "signature": test_sig,
                    "parametrize": parametrize_str,
                    "test_cases": {"list": formatted_test_cases},
                    "body": (
                        f"        result = run_{snake_method_name}(Solution, {call_args})\n"
                        f"        assert_{snake_method_name}(result, expected)"
                    ),
                }
            ]
        }

        # Imports
        typing_imports = []
        for type_name in ["List", "Optional", "Dict", "Set", "Tuple"]:
            if type_name in method_signature:
                typing_imports.append(type_name)

        if typing_imports:
            typing_str = f"from typing import {', '.join(typing_imports)}"
            transformed["solution_imports"] = typing_str
            transformed["test_imports"] = (
                f"import pytest\n{typing_str}\nfrom leetcode_py import logged_test\n"
                f"from .helpers import assert_{snake_method_name}, run_{snake_method_name}\n"
                f"from .solution import Solution"
            )
            transformed["helpers_imports"] = typing_str
        else:
            transformed["solution_imports"] = ""
            transformed["test_imports"] = (
                f"import pytest\nfrom leetcode_py import logged_test\n"
                f"from .helpers import assert_{snake_method_name}, run_{snake_method_name}\n"
                f"from .solution import Solution"
            )
            transformed["helpers_imports"] = ""

    return transformed


def process_problem(slug):
    scrape_slug = slug.replace("_", "-")

    print(f"\n[{slug}] Starting process...")

    try:
        # 1. Scrape
        print(f"[{slug}] Scraping {scrape_slug}...")
        result = subprocess.run(
            ["uv", "run", "python", "-m", "leetcode_py.cli.main", "scrape", "-s", scrape_slug],
            check=False,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(f"[{slug}] Scrape FAILED with code {result.returncode}.")
            return False

        output = result.stdout
        json_start = output.find("{")
        if json_start == -1:
            print(f"[{slug}] Scrape output does not contain JSON start.")
            return False

        json_content = output[json_start:]
        try:
            data = json.loads(json_content)
        except json.JSONDecodeError:
            print(f"[{slug}] Extracted content is not valid JSON.")
            return False

        # TRANSFORM DATA
        transformed_data = transform_scraped_data(data)

        # Convert to snake_case for file naming
        snake_slug = slug.replace("-", "_")

        # If starts with digit, prepend _
        if snake_slug[0].isdigit():
            snake_slug = f"_{snake_slug}"

        # Save to file
        json_dir = "leetcode_py/cli/resources/leetcode/json/problems"
        os.makedirs(json_dir, exist_ok=True)
        json_path = os.path.join(json_dir, f"{snake_slug}.json")

        with open(json_path, "w") as f:
            json.dump(transformed_data, f, indent=2)

        abs_json_path = os.path.abspath(json_path)
        print(f"[{slug}] Scrape successful. Saved to {abs_json_path}")

        # 2. Generate
        print(f"[{snake_slug}] Generating...")
        gen_result = subprocess.run(
            [
                "uv",
                "run",
                "python",
                "-m",
                "leetcode_py.cli.main",
                "gen",
                "-s",
                snake_slug,
                "-o",
                "leetcode",
                "--force",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        if gen_result.returncode != 0:
            print(f"[{slug}] Generation FAILED.")
            print(f"Error output: {gen_result.stderr}")
            print(f"Standard output: {gen_result.stdout}")
            return False

        print(f"[{slug}] Generation successful.")
        return True

    except Exception as e:
        print(f"[{slug}] Unexpected error: {e}")
        return False


def main():
    if not shutil.which("uv"):
        print("Error: 'uv' executable not found in PATH.")
        sys.exit(1)

    slugs = get_missing_slugs()
    print(f"Found {len(slugs)} problems to process.")

    success_count = 0
    failed_slugs = []

    for i, slug in enumerate(slugs):
        print(f"\n--- Processing {i+1}/{len(slugs)}: {slug} ---")
        if process_problem(slug):
            success_count += 1
        else:
            failed_slugs.append(slug)

        time.sleep(0.5)

    print("\n" + "=" * 30)
    print(f"Completed. Success: {success_count}, Failed: {len(failed_slugs)}")

    if failed_slugs:
        print("\nFailed slugs:")
        for s in failed_slugs:
            print(s)

        with open("failed_slugs.txt", "w") as f:
            for s in failed_slugs:
                f.write(s + "\n")
        print("Failed slugs written to failed_slugs.txt")
    else:
        if os.path.exists("failed_slugs.txt"):
            os.remove("failed_slugs.txt")


if __name__ == "__main__":
    main()
