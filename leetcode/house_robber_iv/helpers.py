def run_min_capability(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.min_capability(nums, k)


def assert_min_capability(result: int, expected: int) -> bool:
    assert result == expected
    return True
