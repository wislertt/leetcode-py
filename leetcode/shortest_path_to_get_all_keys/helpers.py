def run_shortest_path_all_keys(solution_class: type, grid: list[str]):
    implementation = solution_class()
    return implementation.shortest_path_all_keys(grid)


def assert_shortest_path_all_keys(result: int, expected: int) -> bool:
    assert result == expected
    return True
