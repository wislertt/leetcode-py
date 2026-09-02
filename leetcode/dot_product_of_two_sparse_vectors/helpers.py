def run_dot_product(solution_class: type, nums1: list[int], nums2: list[int]):
    v1 = solution_class(nums1)
    v2 = solution_class(nums2)
    return v1.dot_product(v2)


def assert_dot_product(result: int, expected: int) -> bool:
    assert result == expected
    return True
