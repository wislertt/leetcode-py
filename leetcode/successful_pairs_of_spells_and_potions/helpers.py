def run_successful_pairs(solution_class: type, spells: list[int], potions: list[int], success: int):
    implementation = solution_class()
    return implementation.successful_pairs(spells, potions, success)


def assert_successful_pairs(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
