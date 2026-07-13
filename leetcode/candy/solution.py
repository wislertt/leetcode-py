class Solution:
    # Time: O(n)
    # Space: O(n)
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Left-to-right: satisfy higher-than-left-neighbor constraint
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left: satisfy higher-than-right-neighbor constraint
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
