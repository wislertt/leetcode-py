def run_optimal_division(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.optimal_division(nums)


def assert_optimal_division(result: str, expected: str) -> bool:
    assert result == expected
    return True
