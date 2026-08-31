def run_sliding_puzzle(solution_class: type, board: list[list[int]]):
    implementation = solution_class()
    return implementation.sliding_puzzle(board)


def assert_sliding_puzzle(result: int, expected: int) -> bool:
    assert result == expected
    return True
