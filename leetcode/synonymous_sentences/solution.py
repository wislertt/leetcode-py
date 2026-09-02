class UnionFind:
    def __init__(self, n: int):
        self.parent: list[int] = list(range(n))
        self.size: list[int] = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


class Solution:
    # Time: O((s + w) * n)
    # Space: O(s + w)
    def generate_sentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        words = sorted({word for pair in synonyms for word in pair})
        index = {word: i for i, word in enumerate(words)}
        uf = UnionFind(len(words))
        for first, second in synonyms:
            uf.union(index[first], index[second])

        groups: dict[int, list[str]] = {}
        for word in words:
            groups.setdefault(uf.find(index[word]), []).append(word)

        sentence = text.split()
        result: list[str] = []
        current: list[str] = []

        def dfs(i: int) -> None:
            if i == len(sentence):
                result.append(" ".join(current))
                return
            word = sentence[i]
            if word in index:
                for alt in groups[uf.find(index[word])]:
                    current.append(alt)
                    dfs(i + 1)
                    current.pop()
            else:
                current.append(word)
                dfs(i + 1)
                current.pop()

        dfs(0)
        return sorted(result)
