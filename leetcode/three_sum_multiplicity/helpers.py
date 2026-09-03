def run_three_sum_multiplicity(solution_class: type, arr: list[int], target: int):
    implementation = solution_class()
    return implementation.three_sum_multiplicity(arr, target)


def assert_three_sum_multiplicity(result: int, expected: int) -> bool:
    assert result == expected
    return True
