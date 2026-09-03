def run_find_duplicate(solution_class: type, paths: list[str]):
    implementation = solution_class()
    return implementation.find_duplicate(paths)


def assert_find_duplicate(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Group order and within-group order do not matter, so compare canonically
    result_sorted = sorted(sorted(group) for group in result)
    expected_sorted = sorted(sorted(group) for group in expected)
    assert result_sorted == expected_sorted
    return True
