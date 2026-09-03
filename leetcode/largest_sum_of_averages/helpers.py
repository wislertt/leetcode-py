def run_largest_sum_of_averages(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.largest_sum_of_averages(nums, k)


def assert_largest_sum_of_averages(result: float, expected: float) -> bool:
    assert abs(result - expected) <= 10**-6
    return True
