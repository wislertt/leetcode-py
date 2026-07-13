def run_shortest_path_binary_matrix(solution_class: type, grid: list[list[int]]):
    implementation = solution_class()
    return implementation.shortest_path_binary_matrix(grid)


def assert_shortest_path_binary_matrix(result: int, expected: int) -> bool:
    assert result == expected
    return True
