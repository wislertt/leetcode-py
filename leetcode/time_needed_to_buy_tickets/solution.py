class Solution:
    # Time: O(n)
    # Space: O(1)
    def time_required_to_buy(self, tickets: list[int], k: int) -> int:
        target = tickets[k]
        total = 0
        for i, need in enumerate(tickets):
            if i <= k:
                total += min(need, target)
            else:
                total += min(need, target - 1)
        return total
