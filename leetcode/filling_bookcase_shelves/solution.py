class Solution:
    # Time: O(n * W)
    # Space: O(n)
    def min_height_shelves(self, books: list[list[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [0] + [10**9] * n
        for i in range(1, n + 1):
            total_w = 0
            max_h = 0
            for j in range(i, 0, -1):
                total_w += books[j - 1][0]
                if total_w > shelf_width:
                    break
                max_h = max(max_h, books[j - 1][1])
                dp[i] = min(dp[i], max_h + dp[j - 1])
        return dp[n]
