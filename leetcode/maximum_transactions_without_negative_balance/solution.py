import heapq


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def max_transactions(self, transactions: list[int]) -> int:
        kept: list[int] = []
        balance = 0
        ans = len(transactions)
        for amount in transactions:
            balance += amount
            heapq.heappush(kept, amount)
            while balance < 0:
                balance -= heapq.heappop(kept)
                ans -= 1
        return ans
