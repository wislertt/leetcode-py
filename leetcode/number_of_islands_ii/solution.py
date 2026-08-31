class UnionFind:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    # Time: O(k * alpha(m * n)) — one union-find pass over positions
    # Space: O(m * n) — parent and size arrays
    def num_islands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        uf = UnionFind(m * n)
        land = set()
        count = 0
        answer: list[int] = []
        for i, j in positions:
            if (i, j) in land:
                answer.append(count)
                continue
            land.add((i, j))
            count += 1
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (x, y) in land and uf.union(i * n + j, x * n + y):
                    count -= 1
            answer.append(count)
        return answer
