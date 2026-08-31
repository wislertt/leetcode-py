class Solution:
    # Time: O(m log m) for sorting the logs
    # Space: O(n)
    def earliest_acq(self, logs: list[list[int]], n: int) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        components = n
        for timestamp, x, y in sorted(logs):
            rx, ry = find(x), find(y)
            if rx == ry:
                continue
            parent[rx] = ry
            components -= 1
            if components == 1:
                return timestamp
        return -1
