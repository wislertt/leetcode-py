import heapq

from leetcode_py import TreeNode


class Solution:
    # Time: O(n log k) where n is the node count
    # Space: O(h + k)
    def closest_k_values(self, root: TreeNode[int], target: float, k: int) -> list[int]:
        heap: list[tuple[float, int]] = []
        stack: list[TreeNode[int]] = []
        node: TreeNode[int] | None = root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            diff = abs(node.val - target)
            if len(heap) < k:
                heapq.heappush(heap, (-diff, node.val))
            elif -heap[0][0] > diff:
                heapq.heapreplace(heap, (-diff, node.val))
            node = node.right
        return [val for _, val in heap]
