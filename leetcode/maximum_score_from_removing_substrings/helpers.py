def run_maximum_gain(solution_class: type, s: str, x: int, y: int):
    implementation = solution_class()
    return implementation.maximum_gain(s, x, y)


def assert_maximum_gain(result: int, expected: int) -> bool:
    assert result == expected
    return True
