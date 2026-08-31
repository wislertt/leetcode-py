def run_group_strings(solution_class: type, strings: list[str]):
    implementation = solution_class()
    return implementation.group_strings(strings)


def assert_group_strings(result: list[list[str]], expected: list[list[str]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = [sorted(group) for group in result]
    expected_sorted = [sorted(group) for group in expected]
    result_sorted.sort()
    expected_sorted.sort()
    assert result_sorted == expected_sorted
    return True
