def run_snakes_and_ladders(solution_class: type, board: list[list[int]]):
    implementation = solution_class()
    return implementation.snakes_and_ladders(board)


def assert_snakes_and_ladders(result: int, expected: int) -> bool:
    assert result == expected
    return True
