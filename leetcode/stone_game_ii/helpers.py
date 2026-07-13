def run_stone_game_ii(solution_class: type, piles: list[int]):
    implementation = solution_class()
    return implementation.stone_game_ii(piles)


def assert_stone_game_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
