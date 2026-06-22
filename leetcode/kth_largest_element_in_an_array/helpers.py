def run_find_kth_largest(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.find_kth_largest(nums, k)


def assert_find_kth_largest(result: int, expected: int) -> bool:
    assert result == expected
    return True
