def run_update_board(solution_class: type, board: list[list[str]], click: list[int]):
    implementation = solution_class()
    return implementation.update_board(board, click)


def assert_update_board(result: list[list[str]], expected: list[list[str]]) -> bool:
    assert result == expected
    return True
