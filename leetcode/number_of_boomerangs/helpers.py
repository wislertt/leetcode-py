def run_number_of_boomerangs(solution_class: type, points: list[list[int]]):
    implementation = solution_class()
    return implementation.number_of_boomerangs(points)


def assert_number_of_boomerangs(result: int, expected: int) -> bool:
    assert result == expected
    return True
