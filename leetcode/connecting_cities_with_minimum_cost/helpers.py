def run_minimum_cost(solution_class: type, n: int, connections: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_cost(n, connections)


def assert_minimum_cost(result: int, expected: int) -> bool:
    assert result == expected
    return True
