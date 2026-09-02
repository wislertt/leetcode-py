class Solution:
    # Time: O(n log n) for the descending sort over n scores
    # Space: O(n) for the placement order and the rank output
    def find_relative_ranks(self, score: list[int]) -> list[str]:
        medals = ("Gold Medal", "Silver Medal", "Bronze Medal")
        order = sorted(range(len(score)), key=score.__getitem__, reverse=True)
        ranks = [""] * len(score)
        for place, idx in enumerate(order):
            ranks[idx] = medals[place] if place < 3 else str(place + 1)
        return ranks
