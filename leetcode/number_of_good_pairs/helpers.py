def run_num_identical_pairs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.num_identical_pairs(nums)


def assert_num_identical_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
