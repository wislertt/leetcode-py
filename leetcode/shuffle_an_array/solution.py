import random


class Solution:
    # Time: O(n) for __init__, reset and shuffle
    # Space: O(n)
    def __init__(self, nums: list[int]) -> None:
        self.original = list(nums)
        self.array = list(nums)

    def reset(self) -> list[int]:
        self.array = list(self.original)
        return list(self.array)

    def shuffle(self) -> list[int]:
        shuffled = list(self.array)
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randrange(i + 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
