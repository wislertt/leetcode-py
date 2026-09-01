from collections import deque


class Solution:
    # Time: O(n) each index enters and leaves both deques at most once
    # Space: O(n) for the two monotonic deques
    def longest_subarray(self, nums: list[int], limit: int) -> int:
        min_deque: deque[int] = deque()
        max_deque: deque[int] = deque()
        left = 0
        best = 0
        for right, value in enumerate(nums):
            while min_deque and min_deque[-1] > value:
                min_deque.pop()
            min_deque.append(value)
            while max_deque and max_deque[-1] < value:
                max_deque.pop()
            max_deque.append(value)
            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            best = max(best, right - left + 1)
        return best
