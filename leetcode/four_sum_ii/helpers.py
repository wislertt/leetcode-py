def run_four_sum_count(
    solution_class: type, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
):
    implementation = solution_class()
    return implementation.four_sum_count(nums1, nums2, nums3, nums4)


def assert_four_sum_count(result: int, expected: int) -> bool:
    assert result == expected
    return True
