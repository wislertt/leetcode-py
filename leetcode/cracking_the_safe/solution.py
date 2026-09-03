class Solution:
    # Time: O(k^n) - each of the k^n edges is visited exactly once
    # Space: O(k^n) - visited set plus the Eulerian path stack
    def crack_safe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(str(d) for d in range(k - 1, -1, -1))

        start = "0" * (n - 1)
        seen: set[str] = set()
        digits: list[str] = []

        def dfs(node: str) -> None:
            for d in range(k):
                edge = node + str(d)
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    digits.append(str(d))

        dfs(start)
        return "".join(digits) + start
