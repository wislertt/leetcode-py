from leetcode_py import TreeNode


def run_count_nodes(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list) if root_list else None
    return implementation.count_nodes(root)


def assert_count_nodes(result: int, expected: int) -> bool:
    assert result == expected
    return True
