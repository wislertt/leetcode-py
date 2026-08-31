def run_two_city_sched_cost(solution_class: type, costs: list[list[int]]):
    implementation = solution_class()
    return implementation.two_city_sched_cost(costs)


def assert_two_city_sched_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
