def run_path_sum(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.path_sum(nums)


def assert_path_sum(result: int, expected: int) -> bool:
    assert result == expected
    return True
