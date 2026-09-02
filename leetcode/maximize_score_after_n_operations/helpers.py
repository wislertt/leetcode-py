def run_max_score(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.max_score(nums)


def assert_max_score(result: int, expected: int) -> bool:
    assert result == expected
    return True
