def run_find_min_step(solution_class: type, board: str, hand: str):
    implementation = solution_class()
    return implementation.find_min_step(board, hand)


def assert_find_min_step(result: int, expected: int) -> bool:
    assert result == expected
    return True
