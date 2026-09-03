def run_find_length(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.find_length(nums1, nums2)


def assert_find_length(result: int, expected: int) -> bool:
    assert result == expected
    return True
