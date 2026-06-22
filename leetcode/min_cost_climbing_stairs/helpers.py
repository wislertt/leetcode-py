def run_min_cost_climbing_stairs(solution_class: type, cost: list[int]):
    implementation = solution_class()
    return implementation.min_cost_climbing_stairs(cost)


def assert_min_cost_climbing_stairs(result: int, expected: int) -> bool:
    assert result == expected
    return True
