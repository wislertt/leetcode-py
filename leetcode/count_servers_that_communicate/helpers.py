def run_count_servers(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.count_servers(grid)


def assert_count_servers(result: int, expected: int) -> bool:
    assert result == expected
    return True
