def run_minimum_cost(solution_class: type, n: int, edges: list[list[int]], query: list[list[int]]):
    implementation = solution_class()
    return implementation.minimum_cost(n, edges, query)


def assert_minimum_cost(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
