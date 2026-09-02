def run_validate_binary_tree_nodes(
    solution_class: type, n: int, left_child: list[int], right_child: list[int]
):
    implementation = solution_class()
    return implementation.validate_binary_tree_nodes(n, left_child, right_child)


def assert_validate_binary_tree_nodes(result: bool, expected: bool) -> bool:
    assert result == expected
    return True
