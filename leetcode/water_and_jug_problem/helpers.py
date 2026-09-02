def run_can_measure_water(solution_class: type, x: int, y: int, target: int):
    implementation = solution_class()
    return implementation.can_measure_water(x, y, target)


def assert_can_measure_water(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
