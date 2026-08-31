class Solution:
    # Time: O(n + p)
    # Space: O(p)
    def are_sentences_similar(
        self, sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        s = {tuple(p) for p in similar_pairs}
        return all(
            x == y or (x, y) in s or (y, x) in s for x, y in zip(sentence1, sentence2, strict=True)
        )
