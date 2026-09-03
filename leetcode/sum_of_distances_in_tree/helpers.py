def run_sum_of_distances_in_tree(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.sum_of_distances_in_tree(n, edges)


def assert_sum_of_distances_in_tree(result: list[int], expected: list[int]) -> bool:
    assert result == expected
    return True
