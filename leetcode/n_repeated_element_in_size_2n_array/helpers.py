def run_repeated_n_times(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.repeated_n_times(nums)


def assert_repeated_n_times(result: int, expected: int) -> bool:
    assert result == expected
    return True
