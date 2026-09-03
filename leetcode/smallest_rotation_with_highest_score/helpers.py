def run_best_rotation(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.best_rotation(nums)


def assert_best_rotation(result: int, expected: int) -> bool:
    assert result == expected
    return True
