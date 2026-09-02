def run_find_difference(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.find_difference(nums1, nums2)


def assert_find_difference(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert sorted(result[0]) == sorted(expected[0])
    assert sorted(result[1]) == sorted(expected[1])
    return True
