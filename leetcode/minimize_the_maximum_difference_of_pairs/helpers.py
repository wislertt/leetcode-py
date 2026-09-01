def run_minimize_max(solution_class: type, nums: list[int], p: int):
    implementation = solution_class()
    return implementation.minimize_max(nums, p)


def assert_minimize_max(result: int, expected: int) -> bool:
    assert result == expected
    return True
