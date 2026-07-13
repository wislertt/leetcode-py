def run_stone_game(solution_class: type, piles: list[int]):
    implementation = solution_class()
    return implementation.stone_game(piles)


def assert_stone_game(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
