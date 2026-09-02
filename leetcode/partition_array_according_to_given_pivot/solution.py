class Solution:
    # Time: O(n)
    # Space: O(n)
    def pivot_array(self, nums: list[int], pivot: int) -> list[int]:
        less: list[int] = []
        equal: list[int] = []
        greater: list[int] = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return [*less, *equal, *greater]
