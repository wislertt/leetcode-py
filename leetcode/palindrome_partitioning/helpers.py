def run_partition(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.partition(s)


def assert_partition(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Only sort the outer list. Inner lists maintain order since substrings must reconstruct s.
    result_sorted = sorted(result)
    expected_sorted = sorted(expected)
    assert result_sorted == expected_sorted
    return True
