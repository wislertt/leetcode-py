def run_max_score(solution_class: type, nums1: list[int], nums2: list[int], k: int):
    implementation = solution_class()
    return implementation.max_score(nums1, nums2, k)


def assert_max_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
