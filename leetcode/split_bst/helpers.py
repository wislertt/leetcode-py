from leetcode_py import TreeNode


def run_split_bst(solution_class: type, root_list: list[int | None], target: int):
    root = TreeNode[int].from_list(root_list)
    implementation = solution_class()
    return implementation.split_bst(root, target)


def assert_split_bst(
    result: list[TreeNode[int] | None], expected_lists: list[list[int | None]]
) -> bool:
    def to_seq(node: TreeNode[int] | None) -> list[int | None]:
        return [] if node is None else node.to_list()

    actual = [to_seq(node) for node in result]
    assert actual == expected_lists
    return True
