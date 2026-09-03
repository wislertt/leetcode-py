def run_advantage_count(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    permutation = implementation.advantage_count(nums1, nums2)
    return permutation, nums1, nums2


def assert_advantage_count(result: tuple[list[int], list[int], list[int]], expected: int) -> bool:
    permutation, nums1, nums2 = result
    assert sorted(permutation) == sorted(nums1)
    gained = sum(p > q for p, q in zip(permutation, nums2, strict=True))
    assert gained == expected
    return True
