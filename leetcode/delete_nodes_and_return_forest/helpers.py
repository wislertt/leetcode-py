from leetcode_py import TreeNode


def run_del_nodes(solution_class: type, root_list: list[int | None], to_delete: list[int]):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.del_nodes(root, to_delete)


def assert_del_nodes(result: list[TreeNode[int]], expected_forest: list[list[int | None]]) -> bool:
    def sort_key(lst: list[int | None]) -> tuple[int, str]:
        return (len(lst), str(lst))

    actual = sorted([node.to_list() for node in result], key=sort_key)
    assert actual == expected_forest
    return True
