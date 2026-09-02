class Solution:
    # Time: O((n + q) log n) - one build pass over the tree plus a descent per query
    # Space: O(n) - segment tree over the building heights
    def leftmost_building_queries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        n = len(heights)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (2 * size)
        tree[size : size + n] = heights
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def next_greater(start: int, limit: int) -> int:
            def descend(node: int, node_lo: int, node_hi: int) -> int:
                if node_hi <= start or tree[node] <= limit:
                    return -1
                if node_lo == node_hi:
                    return node_lo
                mid = (node_lo + node_hi) // 2
                found = descend(2 * node, node_lo, mid)
                return found if found != -1 else descend(2 * node + 1, mid + 1, node_hi)

            if start >= n:
                return -1
            return descend(1, 0, size - 1)

        result: list[int] = []
        for query in queries:
            left, right = query[0], query[1]
            if left > right:
                left, right = right, left
            if left == right:
                result.append(left)
            elif heights[left] < heights[right]:
                result.append(right)
            else:
                result.append(next_greater(right, heights[left]))
        return result
