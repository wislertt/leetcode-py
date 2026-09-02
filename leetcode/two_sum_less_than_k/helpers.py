def run_two_sum_less_than_k(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.two_sum_less_than_k(nums, k)


def assert_two_sum_less_than_k(result: int, expected: int) -> bool:
    assert result == expected
    return True
