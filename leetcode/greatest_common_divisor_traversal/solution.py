class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        self.components -= 1


class Solution:
    # Time: O(n * sqrt(m))
    # Space: O(n)
    def can_traverse_all_pairs(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        uf = UnionFind(n)
        prime_to_index: dict[int, int] = {}

        for index, value in enumerate(nums):
            if value == 1:
                return False
            for factor in self._prime_factors(value):
                if factor in prime_to_index:
                    uf.union(index, prime_to_index[factor])
                else:
                    prime_to_index[factor] = index

        return uf.components == 1

    @staticmethod
    def _prime_factors(value: int) -> set[int]:
        factors: set[int] = set()
        divisor = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                factors.add(divisor)
                while value % divisor == 0:
                    value //= divisor
            divisor += 1
        if value > 1:
            factors.add(value)
        return factors
