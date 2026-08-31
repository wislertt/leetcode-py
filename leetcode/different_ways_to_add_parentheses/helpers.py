def run_diff_ways_to_compute(solution_class: type, expression: str):
    implementation = solution_class()
    return implementation.diff_ways_to_compute(expression)


def assert_diff_ways_to_compute(result: list[int], expected: list[int]) -> bool:
    # Sort both result and expected for comparison since order doesn't matter
    assert sorted(result) == sorted(expected)
    return True
