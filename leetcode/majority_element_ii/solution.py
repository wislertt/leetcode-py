class Solution:
    # Time: O(n)
    # Space: O(1)
    def majority_element(self, nums: list[int]) -> list[int]:
        candidate1 = 0
        candidate2 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        threshold = len(nums) // 3
        result: list[int] = []
        if nums.count(candidate1) > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > threshold:
            result.append(candidate2)

        return result
