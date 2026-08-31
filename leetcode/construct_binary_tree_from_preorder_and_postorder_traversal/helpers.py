from leetcode_py import TreeNode


def run_construct_from_pre_post(solution_class: type, preorder: list[int], postorder: list[int]):
    implementation = solution_class()
    return implementation.construct_from_pre_post(preorder, postorder)


def assert_construct_from_pre_post(result: TreeNode[int] | None, expected: list[list[int]]) -> bool:
    expected_preorder, expected_postorder = expected

    def preorder_traverse(node: TreeNode[int] | None) -> list[int]:
        if not node:
            return []
        return [node.val, *preorder_traverse(node.left), *preorder_traverse(node.right)]

    def postorder_traverse(node: TreeNode[int] | None) -> list[int]:
        if not node:
            return []
        return [*postorder_traverse(node.left), *postorder_traverse(node.right), node.val]

    # Multiple valid trees exist (single-child nodes can lean either way), so
    # validate that the returned tree reproduces both input traversals.
    assert result is not None
    assert preorder_traverse(result) == expected_preorder
    assert postorder_traverse(result) == expected_postorder
    return True
