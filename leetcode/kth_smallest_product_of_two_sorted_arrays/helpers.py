def run_kth_smallest_product(solution_class: type, nums1: list[int], nums2: list[int], k: int):
    implementation = solution_class()
    return implementation.kth_smallest_product(nums1, nums2, k)


def assert_kth_smallest_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
