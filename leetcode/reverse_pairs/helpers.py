def run_reverse_pairs(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.reverse_pairs(nums)


def assert_reverse_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
