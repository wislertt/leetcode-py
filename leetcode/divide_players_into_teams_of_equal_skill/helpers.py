def run_divide_players(solution_class: type, skill: list[int]):
    implementation = solution_class()
    return implementation.divide_players(skill)


def assert_divide_players(result: int, expected: int) -> bool:
    assert result == expected
    return True
