def run_number_of_subarrays(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.number_of_subarrays(nums, k)


def assert_number_of_subarrays(result: int, expected: int) -> bool:
    assert result == expected
    return True
