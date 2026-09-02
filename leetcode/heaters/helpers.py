def run_find_radius(solution_class: type, houses: list[int], heaters: list[int]):
    implementation = solution_class()
    return implementation.find_radius(houses, heaters)


def assert_find_radius(result: int, expected: int) -> bool:
    assert result == expected
    return True
