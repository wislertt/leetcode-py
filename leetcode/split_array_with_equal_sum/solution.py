class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def split_array(self, nums: list[int]) -> bool:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, value in enumerate(nums):
            prefix[i + 1] = prefix[i] + value
        for j in range(3, n - 3):
            left_sums: set[int] = set()
            for i in range(1, j - 1):
                if prefix[i] == prefix[j] - prefix[i + 1]:
                    left_sums.add(prefix[i])
            for k in range(j + 2, n - 1):
                s3 = prefix[k] - prefix[j + 1]
                s4 = prefix[n] - prefix[k + 1]
                if s3 == s4 and s3 in left_sums:
                    return True
        return False
