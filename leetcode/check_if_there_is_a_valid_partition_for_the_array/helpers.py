def run_valid_partition(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.valid_partition(nums)


def assert_valid_partition(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
