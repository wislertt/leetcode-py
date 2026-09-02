from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def get_directions(self, root: TreeNode[int] | None, start_value: int, dest_value: int) -> str:
        def find(node: TreeNode[int] | None, target: int, path: list[str]) -> list[str] | None:
            if node is None:
                return None
            if node.val == target:
                return list(path)
            path.append("L")
            found = find(node.left, target, path)
            if found is not None:
                return found
            path[-1] = "R"
            found = find(node.right, target, path)
            if found is not None:
                return found
            path.pop()
            return None

        if root is None:
            return ""

        start_path = find(root, start_value, [])
        dest_path = find(root, dest_value, [])
        if start_path is None or dest_path is None:
            return ""

        shared = 0
        while (
            shared < len(start_path)
            and shared < len(dest_path)
            and start_path[shared] == dest_path[shared]
        ):
            shared += 1

        return "U" * (len(start_path) - shared) + "".join(dest_path[shared:])
