def run_max_coins(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_coins(nums)


def assert_max_coins(result: int, expected: int) -> bool:
    assert result == expected
    return True
