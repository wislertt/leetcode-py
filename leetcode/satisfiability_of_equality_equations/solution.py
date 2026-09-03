class Solution:
    # Time: O(n * alpha(26))
    # Space: O(26)
    def equations_possible(self, equations: list[str]) -> bool:
        parent: list[int] = list(range(26))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b

        for equation in equations:
            if equation[1] == "=":
                union(ord(equation[0]) - ord("a"), ord(equation[3]) - ord("a"))

        for equation in equations:
            if equation[1] == "!" and find(ord(equation[0]) - ord("a")) == find(
                ord(equation[3]) - ord("a")
            ):
                return False
        return True
