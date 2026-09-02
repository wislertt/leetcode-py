def run_anagram_mappings(solution_class: type, nums1: list[int], nums2: list[int]):
    implementation = solution_class()
    return implementation.anagram_mappings(nums1, nums2)


def assert_anagram_mappings(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
