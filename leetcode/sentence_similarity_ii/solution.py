class Solution:
    # Time: O((n + m) * alpha(n)) for n pairs and m words
    # Space: O(n)
    def are_sentences_similar_two(
        self, sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        parent: dict[str, str] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in similar_pairs:
            parent.setdefault(a, a)
            parent.setdefault(b, b)
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        return all(x == y or find(x) == find(y) for x, y in zip(sentence1, sentence2, strict=True))
