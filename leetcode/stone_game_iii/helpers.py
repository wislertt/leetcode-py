def run_stone_game_iii(solution_class: type, stone_value: list[int]):
    implementation = solution_class()
    return implementation.stone_game_iii(stone_value)


def assert_stone_game_iii(result: str, expected: str) -> bool:
    assert result == expected
    return True
