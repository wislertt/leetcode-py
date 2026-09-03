def run_max_vacation_days(solution_class: type, flights: list[list[int]], days: list[list[int]]):
    implementation = solution_class()
    return implementation.max_vacation_days(flights, days)


def assert_max_vacation_days(result: int, expected: int) -> bool:
    assert result == expected
    return True
