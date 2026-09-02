class Solution:
    # Time: O(n)
    # Space: O(1)
    def increasing_triplet(self, nums: list[int]) -> bool:
        first: int | None = None
        second: int | None = None
        for x in nums:
            if first is None or x <= first:
                first = x
            elif second is None or x <= second:
                second = x
            else:
                return True
        return False
