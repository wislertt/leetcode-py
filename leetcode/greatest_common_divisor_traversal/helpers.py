def run_can_traverse_all_pairs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.can_traverse_all_pairs(nums)


def assert_can_traverse_all_pairs(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
