from leetcode_py import TreeNode


def run_sorted_array_to_bst(solution_class: type, nums: list[int]):
    implementation = solution_class()
    return implementation.sorted_array_to_bst(nums)


def assert_sorted_array_to_bst(result: TreeNode[int] | None, nums: list[int]) -> bool:
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

    assert inorder(result) == nums
    assert is_balanced(result)
    return True
