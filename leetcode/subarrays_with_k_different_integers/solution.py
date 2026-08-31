class Solution:
    # Time: O(n)
    # Space: O(n)
    def subarrays_with_k_distinct(self, nums: list[int], k: int) -> int:
        def at_most(target: int) -> int:
            if target < 0:
                return 0
            count: dict[int, int] = {}
            left = 0
            total = 0
            for right, num in enumerate(nums):
                count[num] = count.get(num, 0) + 1
                while len(count) > target:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                total += right - left + 1
            return total

        return at_most(k) - at_most(k - 1)
