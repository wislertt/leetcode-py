class Solution:
    # Time: O(n) where n = len(nums); each node is visited once
    # Space: O(n) for the node lookup map plus O(depth) recursion
    def path_sum(self, nums: list[int]) -> int:
        # Node key is depth * 10 + position; value is the units digit
        nodes = {num // 10: num % 10 for num in nums}
        total = 0
        stack: list[tuple[int, int]] = [(11, 0)]
        while stack:
            node, running = stack.pop()
            if node not in nodes:
                continue
            running += nodes[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + pos * 2 - 1
            right = left + 1
            if left in nodes or right in nodes:
                stack.append((left, running))
                stack.append((right, running))
            else:
                total += running
        return total
