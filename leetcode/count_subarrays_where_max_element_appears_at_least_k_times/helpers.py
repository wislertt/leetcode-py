def run_count_subarrays(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.count_subarrays(nums, k)


def assert_count_subarrays(result: int, expected: int) -> bool:
    assert result == expected
    return True
