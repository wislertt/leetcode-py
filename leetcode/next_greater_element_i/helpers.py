def run_next_greater_element(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.next_greater_element(nums1, nums2)


def assert_next_greater_element(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
