def run_candy_crush(solution_class: type, board: list[list[int]]):
    implementation = solution_class()
    return implementation.candy_crush(board)


def assert_candy_crush(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
