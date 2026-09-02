def run_median_sliding_window(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.median_sliding_window(nums, k)


def assert_median_sliding_window(result: list[float], expected: list[float]) -> bool:
    assert result == expected
    return True
