def run_find_paths(
    solution_class: type, m: int, n: int, max_move: int, start_row: int, start_column: int
):
    implementation = solution_class()
    return implementation.find_paths(m, n, max_move, start_row, start_column)


def assert_find_paths(result: int, expected: int) -> bool:
    assert result == expected
    return True
