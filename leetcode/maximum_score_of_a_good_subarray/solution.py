class Solution:
    # Time: O(n)
    # Space: O(1)
    def maximum_score(self, nums: list[int], k: int) -> int:
        left = right = k
        cur_min = nums[k]
        best = cur_min
        while left > 0 or right < len(nums) - 1:
            next_left = nums[left - 1] if left > 0 else 0
            next_right = nums[right + 1] if right < len(nums) - 1 else 0
            if next_left >= next_right:
                left -= 1
            else:
                right += 1
            cur_min = min(cur_min, max(next_left, next_right))
            best = max(best, cur_min * (right - left + 1))
        return best
