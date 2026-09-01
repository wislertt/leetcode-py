def run_winner_of_game(solution_class: type, colors: str):
    implementation = solution_class()
    return implementation.winner_of_game(colors)


def assert_winner_of_game(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
