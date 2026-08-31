from collections import deque


class Solution:
    # Time: O(n)
    # Space: O(n)
    def shortest_subarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num
        result = n + 1
        queue: deque[int] = deque()
        for j in range(n + 1):
            while queue and prefix[j] - prefix[queue[0]] >= k:
                result = min(result, j - queue.popleft())
            while queue and prefix[queue[-1]] >= prefix[j]:
                queue.pop()
            queue.append(j)
        return result if result <= n else -1
