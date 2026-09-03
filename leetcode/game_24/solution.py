from fractions import Fraction


class Solution:
    # Time: O(n^3 * 4^(n-1)) with n = 4, a constant bounded by ~6 * 4^5 pairings
    # Space: O(4^2) for the memoized intermediate states
    def judge_point24(self, cards: list[int]) -> bool:
        memo: dict[tuple[Fraction, ...], bool] = {}

        def search(values: tuple[Fraction, ...]) -> bool:
            if len(values) == 1:
                return values[0] == Fraction(24)
            cached = memo.get(values)
            if cached is not None:
                return cached
            n = len(values)
            result = False
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    rest = [values[k] for k in range(n) if k not in (i, j)]
                    a, b = values[i], values[j]
                    results = [a + b, a - b, a * b]
                    if b != 0:
                        results.append(a / b)
                    if any(search((*rest, nxt)) for nxt in results):
                        result = True
                        break
                if result:
                    break
            memo[values] = result
            return result

        return search(tuple(Fraction(card) for card in cards))
