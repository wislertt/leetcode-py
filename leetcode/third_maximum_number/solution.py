class Solution:
    # Time: O(n)
    # Space: O(1)
    def third_max(self, nums: list[int]) -> int:
        top: list[int] = []
        for num in nums:
            if num in top:
                continue
            top.append(num)
            top.sort(reverse=True)
            if len(top) > 3:
                top.pop()
        return top[2] if len(top) > 2 else top[0]
