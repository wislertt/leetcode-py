def run_ship_within_days(solution_class: type, weights: list[int], days: int):
    implementation = solution_class()
    return implementation.ship_within_days(weights, days)


def assert_ship_within_days(result: int, expected: int) -> bool:
    assert result == expected
    return True
