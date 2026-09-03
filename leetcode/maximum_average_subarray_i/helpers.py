def run_find_max_average(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.find_max_average(nums, k)


def assert_find_max_average(result: float, expected: float) -> bool:
    assert abs(result - expected) < 10**-4
    return True
