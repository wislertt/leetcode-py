def run_min_cost_tickets(solution_class: type, days: list[int], costs: list[int]):
    implementation = solution_class()
    return implementation.min_cost_tickets(days, costs)


def assert_min_cost_tickets(result: int, expected: int) -> bool:
    assert result == expected
    return True
