def run_get_final_state(solution_class: type, nums: list[int], k: int, multiplier: int):
    implementation = solution_class()
    return implementation.get_final_state(nums, k, multiplier)


def assert_get_final_state(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
