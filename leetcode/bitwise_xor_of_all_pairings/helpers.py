def run_xor_all_nums(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.xor_all_nums(nums1, nums2)


def assert_xor_all_nums(result: int, expected: int) -> bool:
    assert result == expected
    return True
