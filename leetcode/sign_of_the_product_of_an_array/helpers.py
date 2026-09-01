def run_array_sign(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.array_sign(nums)


def assert_array_sign(result: int, expected: int) -> bool:
    assert result == expected
    return True
