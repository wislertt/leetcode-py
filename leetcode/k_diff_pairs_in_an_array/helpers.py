def run_find_pairs(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.find_pairs(nums, k)


def assert_find_pairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
