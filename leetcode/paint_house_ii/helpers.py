def run_min_cost_ii(solution_class: type, costs: list[list[int]]):
    implementation = solution_class()
    return implementation.min_cost_ii(costs)


def assert_min_cost_ii(result: int, expected: int) -> bool:
    assert result == expected
    return True
