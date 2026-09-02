class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_operations(self, logs: list[str]) -> int:
        depth = 0
        for op in logs:
            if op == "../":
                depth = max(0, depth - 1)
            elif op != "./":
                depth += 1
        return depth
