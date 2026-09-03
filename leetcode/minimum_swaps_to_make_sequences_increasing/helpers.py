def run_min_swap(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.min_swap(nums1, nums2)


def assert_min_swap(result: int, expected: int) -> bool:
    assert result == expected
    return True
