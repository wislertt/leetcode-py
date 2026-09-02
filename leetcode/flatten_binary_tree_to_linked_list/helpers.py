from leetcode_py import TreeNode


def run_flatten(solution_class: type, root_list: list[int | None]):
    implementation = solution_class()
    root = TreeNode.from_list(root_list)
    implementation.flatten(root)
    if root is None:
        return []
    return root.to_list()


def assert_flatten(result: list[int | None], expected: list[int | None]) -> bool:
    assert result == expected
    return True
