def run_count_strictly_increasing(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.count_strictly_increasing(nums)


def assert_count_strictly_increasing(result: int, expected: int) -> bool:
    assert result == expected
    return True
