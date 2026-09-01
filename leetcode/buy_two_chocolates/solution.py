class Solution:
    # Time: O(n)
    # Space: O(1)
    def buy_choco(self, prices: list[int], money: int) -> int:
        first = second = 101
        for price in prices:
            if price < first:
                second = first
                first = price
            elif price < second:
                second = price
        total = first + second
        return money - total if total <= money else money
