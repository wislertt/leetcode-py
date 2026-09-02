def run_calculate_minimum_hp(solution_class: type, dungeon: list[list[int]]):
    implementation = solution_class()
    return implementation.calculate_minimum_hp(dungeon)


def assert_calculate_minimum_hp(result: int, expected: int) -> bool:
    assert result == expected
    return True
