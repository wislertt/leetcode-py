def run_k_smallest_pairs(solution_class: type, nums1: list[int], nums2: list[int], k: int):
    implementation = solution_class()
    return implementation.k_smallest_pairs(nums1, nums2, k)


def assert_k_smallest_pairs(result: list[list[int]], expected: list[list[int]]) -> bool:
    # Order of pairs with equal sums may vary, so compare as multisets
    assert sorted(result) == sorted(expected)
    return True
