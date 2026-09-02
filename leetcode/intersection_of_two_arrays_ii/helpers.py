def run_intersection(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.intersection(nums1, nums2)


def assert_intersection(result: list[int], expected: list[int]) -> bool:
    assert sorted(result) == sorted(expected)
    return True
