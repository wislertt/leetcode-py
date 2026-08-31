def run_max_sub_array_len(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.max_sub_array_len(nums, k)


def assert_max_sub_array_len(result: int, expected: int) -> bool:
    assert result == expected
    return True
