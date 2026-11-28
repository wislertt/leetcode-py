# TODO: temporary use only while completing ongoing list

# Pick priority (--take waterfall):
#   1. unscrapable todo queue (UNSCRAPABLE_QUEUE in unscrapable.py) — drain it first
#   2. registered problem lists (best list = lowest missing count)
#   3. fallback: lowest LeetCode number not in the database at all (no tag; if the
#      scrape later proves it non-Python, the caller files it in NON_PYTHON_PROBLEMS)

import argparse
import sys
from pathlib import Path

# Import the problem lists
sys.path.append(str(Path(__file__).parent.parent.parent))
from problem_lists import available_lists
from problem_lists.unscrapable import (
    get_non_python_numbers,
    get_unscrapable_numbers,
    get_unscrapable_queue,
)
from problem_lists.utils import get_existing_problems

# Upper bound of LeetCode problem numbers for the fallback scan. Bump manually as
# LeetCode adds problems (check leetcode.com/problemset total when the fallback
# starts returning nothing).
FALLBACK_MAX_PROBLEM = 3600


def get_missing_by_list(existing_problems: set[int]) -> dict[str, list[int]]:
    """Compute the sorted missing problems per list, excluding unscrapable ones."""
    unscrapable_numbers = get_unscrapable_numbers()
    missing_by_list = {}
    for tag_name, problem_tuples in available_lists.items():
        problem_numbers = {num for num, _ in problem_tuples}
        missing = sorted(problem_numbers - existing_problems - unscrapable_numbers)
        if missing:
            missing_by_list[tag_name] = missing
    return missing_by_list


def _list_tag_for_number(number: int) -> str | None:
    """First registered list containing this number, or None."""
    for tag_name, problem_tuples in available_lists.items():
        if any(num == number for num, _ in problem_tuples):
            return tag_name
    return None


def _name_in_list(number: int, tag_name: str) -> str | None:
    return next((name for num, name in available_lists[tag_name] if num == number), None)


def get_next_problem(tag_names=None):
    """Get the next problem to work on from the list with the lowest missing problems."""
    if tag_names is None:
        tag_names = list(available_lists.keys())

    existing_problems = get_existing_problems()

    # Find the list with the lowest missing problems
    best_list = None
    min_missing = float("inf")
    missing_problems = []

    for tag_name, missing in get_missing_by_list(existing_problems).items():
        if tag_name in tag_names:
            missing_count = len(missing)

            if missing_count > 0 and missing_count < min_missing:
                min_missing = missing_count
                best_list = tag_name
                missing_problems = missing

    if not missing_problems or best_list is None:
        print("No missing problems found in any of the specified lists!")
        return None

    # Get the first missing problem from the best list
    next_problem_number = missing_problems[0]

    result = {
        "tag_name": best_list,
        "problem_number": next_problem_number,
        "problem_name": _name_in_list(next_problem_number, best_list),
        "missing_count": min_missing,
        "total_in_list": len(available_lists[best_list]),
    }

    return result


def get_next_problems(count: int) -> list[dict]:
    """Get the next `count` problems across the full waterfall, consuming each pick.

    Sources, in priority order:
      1. unscrapable todo queue (UNSCRAPABLE_QUEUE entries; source='unscrapable') —
         tagged with its list membership if any, else no tag
      2. registered problem lists via the best-list rule (source='list')
      3. lowest LeetCode number not in the database at all (source='new') —
         never tagged; scrape failure routing is the caller's job

    Non-Python (SQL/shell) numbers are never picked. Queue entries that already
    exist as problems are skipped as stale.
    """
    existing = get_existing_problems()
    non_python = get_non_python_numbers()
    queue = [
        (num, name)
        for num, name in get_unscrapable_queue()
        if num not in existing and num not in non_python
    ]

    missing_by_list = get_missing_by_list(existing)
    # Fallback pool: every database-absent number no list claims and no
    # unscrapable/non-python record covers
    all_list_numbers = {num for tuples in available_lists.values() for num, _ in tuples}
    fallback = sorted(
        set(range(1, FALLBACK_MAX_PROBLEM + 1))
        - existing
        - get_unscrapable_numbers()
        - non_python
        - all_list_numbers
    )

    results = []

    for _ in range(count):
        source = _next_pick(queue, missing_by_list, fallback)
        if source is None:
            break
        kind, number, name = source
        for missing in missing_by_list.values():
            if number in missing:
                missing.remove(number)

        if kind == "unscrapable":
            tag = _list_tag_for_number(number) or "none"
        elif kind == "list":
            tag = _list_tag_for_number(number)
            name = _name_in_list(number, tag) if tag else None
        else:
            tag = "none"  # no tag for database-absent problems; scrape reveals the name

        results.append(
            {
                "problem_number": number,
                "problem_name": name,
                "tag_name": tag,
                "source": kind,
            }
        )

    return results


def _next_pick(queue, missing_by_list, fallback):
    """Next (source_kind, number, name) respecting priority; consumes the pick."""
    if queue:
        num, name = queue.pop(0)
        return "unscrapable", num, name

    best_tag = min(missing_by_list, key=lambda t: len(missing_by_list[t]), default=None)
    if best_tag and missing_by_list.get(best_tag):
        return "list", missing_by_list[best_tag].pop(0), None

    if fallback:
        return "new", fallback.pop(0), None

    return None


def main():
    parser = argparse.ArgumentParser(description="Get the next missing problem(s) to work on.")
    parser.add_argument(
        "--take",
        type=int,
        metavar="N",
        help="print the next N problems, one per line as 'NUMBER TAG NAME SOURCE' "
        "(source: unscrapable|list|new), with each pick virtually consumed so no "
        "number repeats",
    )
    args = parser.parse_args()

    if args.take is not None:
        for problem in get_next_problems(args.take):
            name = problem["problem_name"] or "(unknown until scraped)"
            print(f"{problem['problem_number']} {problem['tag_name']} {name} {problem['source']}")
        return

    next_problem = get_next_problem()
    if next_problem:
        completed = next_problem["total_in_list"] - next_problem["missing_count"]
        total = next_problem["total_in_list"]
        percentage = completed / total * 100

        print("\n🎯 Next problem to work on:")
        print(f"   Problem #{next_problem['problem_number']} - {next_problem['problem_name']}")
        print(f"   Tag: {next_problem['tag_name']}")
        print(f"   Progress: {completed}/{total} ({percentage:.1f}%)")


if __name__ == "__main__":
    main()
