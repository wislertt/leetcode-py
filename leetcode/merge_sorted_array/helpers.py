def run_merge(solution_class: type, nums1: list[int], m: int, nums2: list[int], n: int):
    implementation = solution_class()
    nums1_copy = nums1[:]
    implementation.merge(nums1_copy, m, nums2, n)
    return nums1_copy


def assert_merge(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
