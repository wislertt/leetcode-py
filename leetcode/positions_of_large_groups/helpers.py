def run_large_group_positions(solution_class: type, s: str):
    implementation = solution_class()
    return implementation.large_group_positions(s)


def assert_large_group_positions(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
