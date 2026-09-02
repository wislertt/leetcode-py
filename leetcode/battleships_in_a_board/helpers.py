def run_count_battleships(solution_class: type, board: list[list[str]]):
    implementation = solution_class()
    return implementation.count_battleships(board)


def assert_count_battleships(result: int, expected: int) -> bool:
    assert result == expected
    return True
