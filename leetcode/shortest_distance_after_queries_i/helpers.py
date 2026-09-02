def run_shortest_distance_after_queries(solution_class: type, n: int, queries: list[list[int]]):
    implementation = solution_class()
    return implementation.shortest_distance_after_queries(n, queries)


def assert_shortest_distance_after_queries(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
