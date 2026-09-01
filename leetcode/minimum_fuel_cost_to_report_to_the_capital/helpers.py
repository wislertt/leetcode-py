def run_minimum_fuel_cost(solution_class: type, roads: list[list[int]], seats: int):
    implementation = solution_class()
    return implementation.minimum_fuel_cost(roads, seats)


def assert_minimum_fuel_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
