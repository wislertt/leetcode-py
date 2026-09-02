def run_find_smallest_set_of_vertices(solution_class: type, n: int, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.find_smallest_set_of_vertices(n, edges)


def assert_find_smallest_set_of_vertices(result: list[int], expected: list[int]) -> bool:
    # LeetCode accepts the vertices in any order, so compare sorted
    assert sorted(result) == expected
    return True
