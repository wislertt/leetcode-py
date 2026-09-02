from leetcode_py import TreeNode


class Solution:
    # Time: O(n) - one pass to link nodes, one pass over created nodes to find the root
    # Space: O(n) - one TreeNode per unique value plus the children set
    def create_binary_tree(self, descriptions: list[list[int]]) -> TreeNode[int] | None:
        nodes: dict[int, TreeNode[int]] = {}
        children: set[int] = set()

        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            children.add(child)

        for val, node in nodes.items():
            if val not in children:
                return node
        return None
