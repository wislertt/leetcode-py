def run_max_number(solution_class: type, nums1: list[int], nums2: list[int], k: int):
    implementation = solution_class()
    return implementation.max_number(nums1, nums2, k)


def assert_max_number(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
