class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def find_number_of_lis(self, nums: list[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        best = max(length)
        return sum(c for length_i, c in zip(length, count, strict=True) if length_i == best)
