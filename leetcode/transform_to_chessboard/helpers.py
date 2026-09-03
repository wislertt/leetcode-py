def run_moves_to_chessboard(solution_class: type, board: list[list[int]]):
    import copy

    board_copy = copy.deepcopy(board)
    implementation = solution_class()
    return implementation.moves_to_chessboard(board_copy)


def assert_moves_to_chessboard(result: int, expected: int) -> bool:
    assert result == expected
    return True
