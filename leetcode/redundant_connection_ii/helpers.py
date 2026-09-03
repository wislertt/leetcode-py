def run_find_redundant_directed_connection(solution_class: type, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.find_redundant_directed_connection(edges)


def assert_find_redundant_directed_connection(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
