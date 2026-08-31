def run_trap_rain_water(solution_class: type, height_map: list[list[int]]):
    implementation = solution_class()
    return implementation.trap_rain_water(height_map)


def assert_trap_rain_water(result: int, expected: int) -> bool:
    assert result == expected
    return True
