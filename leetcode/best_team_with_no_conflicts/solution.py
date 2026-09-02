class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def best_team_score(self, scores: list[int], ages: list[int]) -> int:
        pairs = sorted(zip(scores, ages, strict=True), key=lambda p: (p[1], p[0]))
        ranks = {score: i for i, score in enumerate(sorted(set(scores)))}
        size = len(ranks)
        tree: list[int] = [0] * (size + 1)

        def update(index: int, value: int) -> None:
            index += 1
            while index <= size:
                tree[index] = max(tree[index], value)
                index += index & (-index)

        def query(index: int) -> int:
            index += 1
            best = 0
            while index > 0:
                best = max(best, tree[index])
                index -= index & (-index)
            return best

        result = 0
        for score, _age in pairs:
            current = query(ranks[score]) + score
            result = max(result, current)
            update(ranks[score], current)
        return result
