def run_jump(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.jump(nums)


def assert_jump(result: int, expected: int) -> bool:
    assert result == expected
    return True
