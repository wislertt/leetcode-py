class Solution:
    # Time: O(n)
    # Space: O(n)
    def best_rotation(self, nums: list[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        for i, val in enumerate(nums):
            # nums[i] earns a point for rotation k exactly when val <= (i - k) % n,
            # which holds over the circular interval of k: [(i + 1) % n, (i - val + 1) % n)
            start = (i + 1) % n
            end = (i - val + 1) % n
            diff[start] += 1
            diff[end] -= 1
        best_k = 0
        best_score = -1
        score = 0
        for k in range(n):
            score += diff[k]
            if score > best_score:
                best_score = score
                best_k = k
        return best_k
