def run_maximum_gap(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.maximum_gap(nums)


def assert_maximum_gap(result: int, expected: int) -> bool:
    assert result == expected
    return True
