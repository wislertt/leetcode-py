def run_min_moves(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.min_moves(nums)


def assert_min_moves(result: int, expected: int) -> bool:
    assert result == expected
    return True
