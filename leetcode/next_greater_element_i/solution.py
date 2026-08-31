class Solution:
    # Time: O(n1 + n2)
    # Space: O(n2)
    def next_greater_element(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater: dict[int, int] = {}
        stack: list[int] = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]
