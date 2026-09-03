def run_min_refuel_stops(
    solution_class: type, target: int, start_fuel: int, stations: list[list[int]]
):
    implementation = solution_class()
    return implementation.min_refuel_stops(target, start_fuel, stations)


def assert_min_refuel_stops(result: int, expected: int) -> bool:
    assert result == expected
    return True
