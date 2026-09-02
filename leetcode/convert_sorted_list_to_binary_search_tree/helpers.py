from leetcode_py import ListNode, TreeNode


def run_sorted_list_to_bst(solution_class: type, head_vals: list[int]):
    head = ListNode[int].from_list(head_vals)
    implementation = solution_class()
    return implementation.sorted_list_to_bst(head)


def assert_sorted_list_to_bst(result: TreeNode[int] | None, head_vals: list[int]) -> bool:
    def inorder(node: TreeNode[int] | None) -> list[int]:
        if node is None:
            return []
        return [*inorder(node.left), node.val, *inorder(node.right)]

    def height(node: TreeNode[int] | None) -> int:
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def is_balanced(node: TreeNode[int] | None) -> bool:
        if node is None:
            return True
        if abs(height(node.left) - height(node.right)) > 1:
            return False
        return is_balanced(node.left) and is_balanced(node.right)

    assert inorder(result) == head_vals
    assert is_balanced(result)
    return True
