class Solution:
    def num_of_subarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        target = k * threshold
        count = 1 if window >= target else 0
        for i in range(k, len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                count += 1
        return count
