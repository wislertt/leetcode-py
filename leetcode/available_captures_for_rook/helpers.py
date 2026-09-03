def run_num_rook_captures(solution_class: type, board: list[list[str]]):
    implementation = solution_class()
    return implementation.num_rook_captures(board)


def assert_num_rook_captures(result: int, expected: int) -> bool:
    assert result == expected
    return True
