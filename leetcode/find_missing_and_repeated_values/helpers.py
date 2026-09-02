def run_find_missing_and_repeated_values(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.find_missing_and_repeated_values(grid)


def assert_find_missing_and_repeated_values(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
