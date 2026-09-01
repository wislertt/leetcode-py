class Solution:
    # Time: O(n) - each index is pushed and popped at most once
    # Space: O(n) - for the index stack
    def final_prices(self, prices: list[int]) -> list[int]:
        answer = list(prices)
        stack: list[int] = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                answer[stack.pop()] -= price
            stack.append(i)
        return answer
