class Solution:
    # Time: O(k * 2^n)
    # Space: O(n)
    def can_partition_k_subsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index: int) -> bool:
            if index == len(nums):
                return True
            for bucket_index in range(k):
                if buckets[bucket_index] + nums[index] <= target:
                    buckets[bucket_index] += nums[index]
                    if backtrack(index + 1):
                        return True
                    buckets[bucket_index] -= nums[index]
                # Prune: empty bucket means placement here is symmetric to any
                # other empty bucket; also a just-filled bucket that failed.
                if buckets[bucket_index] == 0:
                    break
            return False

        return backtrack(0)
