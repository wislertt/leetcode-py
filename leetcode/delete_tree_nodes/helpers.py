def run_delete_tree_nodes(solution_class: type, nodes: int, parent: list[int], value: list[int]):
    implementation = solution_class()
    return implementation.delete_tree_nodes(nodes, parent, value)


def assert_delete_tree_nodes(result: int, expected: int) -> bool:
    assert result == expected
    return True
