def run_smallest_distance_pair(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.smallest_distance_pair(nums, k)


def assert_smallest_distance_pair(result: int, expected: int) -> bool:
    assert result == expected
    return True
