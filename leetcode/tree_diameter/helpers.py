def run_tree_diameter(solution_class: type, edges: list[list[int]]):
    implementation = solution_class()
    return implementation.tree_diameter(edges)


def assert_tree_diameter(result: int, expected: int) -> bool:
    assert result == expected
    return True
