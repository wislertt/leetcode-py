class Solution:
    # Time: O(n^2 * total_sum) subset-sum over (size, sum) pairs
    # Space: O(n * total_sum)
    def split_array_same_average(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if n == 1:
            return False
        # avg(A) == avg(B) implies avg(A) == avg(nums); check each size k
        # for a subset whose sum equals k * total / n
        sums_by_size: list[set[int]] = [set() for _ in range(n + 1)]
        sums_by_size[0].add(0)
        for num in nums:
            for k in range(n - 1, 0, -1):
                for s in sums_by_size[k - 1]:
                    sums_by_size[k].add(s + num)
        for k in range(1, n // 2 + 1):
            if total * k % n == 0 and total * k // n in sums_by_size[k]:
                return True
        return False
