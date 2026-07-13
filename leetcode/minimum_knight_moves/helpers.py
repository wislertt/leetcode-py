def run_min_knight_moves(solution_class: type, x: int, y: int):
    implementation = solution_class()
    return implementation.min_knight_moves(x, y)


def assert_min_knight_moves(result: int, expected: int) -> bool:
    assert result == expected
    return True
