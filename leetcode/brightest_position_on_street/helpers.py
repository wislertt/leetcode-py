def run_brightest_position(solution_class: type, lights: list[list[int]]):
    implementation = solution_class()
    return implementation.brightest_position(lights)


def assert_brightest_position(result: int, expected: int) -> bool:
    assert result == expected
    return True
