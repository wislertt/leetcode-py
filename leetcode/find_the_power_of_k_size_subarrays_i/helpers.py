def run_results_array(solution_class: type, nums: list[int], k: int):
    implementation = solution_class()
    return implementation.results_array(nums, k)


def assert_results_array(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
