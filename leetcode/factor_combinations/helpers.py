def run_get_factors(solution_class: type, n: int):
    implementation = solution_class()
    return implementation.get_factors(n)


def assert_get_factors(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    result_sorted = sorted(sorted(combo) for combo in result)
    expected_sorted = sorted(sorted(combo) for combo in expected)
    assert result_sorted == expected_sorted
    return True
