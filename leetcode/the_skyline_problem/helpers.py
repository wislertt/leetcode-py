def run_get_skyline(solution_class: type, buildings: list[list[int]]):
    implementation = solution_class()
    return implementation.get_skyline(buildings)


def assert_get_skyline(result: list[list[int]], expected: list[list[int]]) -> bool:
    assert result == expected
    return True
