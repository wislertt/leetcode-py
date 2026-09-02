class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def outer_trees(self, trees: list[list[int]]) -> list[list[int]]:
        points = sorted(tuple(p) for p in trees)

        def cross(i: int, j: int, k: int) -> int:
            a, b, c = points[i], points[j], points[k]
            return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

        n = len(points)
        if n < 4:
            return [list(p) for p in points]

        visited = [False] * n
        stack = [0]
        for i in range(1, n):
            while len(stack) > 1 and cross(stack[-2], stack[-1], i) < 0:
                visited[stack.pop()] = False
            visited[i] = True
            stack.append(i)

        lower_hull_size = len(stack)
        for i in range(n - 2, -1, -1):
            if visited[i]:
                continue
            while len(stack) > lower_hull_size and cross(stack[-2], stack[-1], i) < 0:
                stack.pop()
            stack.append(i)

        stack.pop()
        return [list(points[i]) for i in stack]
