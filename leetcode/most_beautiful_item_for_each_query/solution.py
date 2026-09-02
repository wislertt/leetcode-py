from bisect import bisect_right


class Solution:
    # Time: O(n log n + m log n) for n items and m queries
    # Space: O(n)
    def maximum_beauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items = sorted(items)
        prices: list[int] = []
        best: list[int] = []
        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            prices.append(price)
            best.append(max_beauty)
        result: list[int] = []
        for query in queries:
            i = bisect_right(prices, query)
            result.append(best[i - 1] if i > 0 else 0)
        return result
