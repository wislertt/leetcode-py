def run_max_uncrossed_lines(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.max_uncrossed_lines(nums1, nums2)


def assert_max_uncrossed_lines(result: int, expected: int) -> bool:
    assert result == expected
    return True
