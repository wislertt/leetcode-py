def run_game_of_life(solution_class: type, board: list[list[int]]):
    import copy

    board_copy = copy.deepcopy(board)
    implementation = solution_class()
    implementation.game_of_life(board_copy)
    return board_copy


def assert_game_of_life(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
