def run_valid_tic_tac_toe(solution_class: type, board: list[str]):
    implementation = solution_class()
    return implementation.valid_tic_tac_toe(board)


def assert_valid_tic_tac_toe(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
