def run_check_move(
    solution_class: type, board: list[list[str]], r_move: int, c_move: int, color: str
):
    implementation = solution_class()
    return implementation.check_move(board, r_move, c_move, color)


def assert_check_move(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
