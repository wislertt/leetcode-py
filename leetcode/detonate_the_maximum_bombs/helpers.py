def run_maximum_detonation(solution_class: type, bombs: list[list[int]]):
    implementation = solution_class()
    return implementation.maximum_detonation(bombs)


def assert_maximum_detonation(result: int, expected: int) -> bool:
    assert result == expected
    return True
