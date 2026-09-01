def run_merge_arrays(solution_class: type, nums1: list[list[int]], nums2: list[list[int]]):
    implementation = solution_class()
    return implementation.merge_arrays(nums1, nums2)


def assert_merge_arrays(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
