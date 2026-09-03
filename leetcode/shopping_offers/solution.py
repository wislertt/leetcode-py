from functools import cache


class Solution:
    # Time: O(len(special) * product(needs[i] + 1))
    # Space: O(product(needs[i] + 1)) for the memo
    def shopping_offers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        offers = [
            (tuple(offer[:-1]), offer[-1])
            for offer in special
            if sum(a * b for a, b in zip(offer[:-1], price, strict=True)) > offer[-1]
        ]

        @cache
        def dfs(need: tuple[int, ...]) -> int:
            best = sum(p * c for p, c in zip(price, need, strict=True))
            for items, cost in offers:
                if all(have >= take for have, take in zip(need, items, strict=True)):
                    rest = tuple(have - take for have, take in zip(need, items, strict=True))
                    best = min(best, cost + dfs(rest))
            return best

        return dfs(tuple(needs))
