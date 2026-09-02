class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def count_smaller(self, nums: list[int]) -> list[int]:
        counts = [0] * len(nums)
        indices = list(range(len(nums)))

        def merge_sort(lo: int, hi: int) -> None:
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            merge_sort(lo, mid)
            merge_sort(mid, hi)

            merged: list[int] = []
            i, j = lo, mid
            while i < mid and j < hi:
                if nums[indices[j]] < nums[indices[i]]:
                    merged.append(indices[j])
                    j += 1
                else:
                    counts[indices[i]] += j - mid
                    merged.append(indices[i])
                    i += 1
            while i < mid:
                counts[indices[i]] += j - mid
                merged.append(indices[i])
                i += 1
            while j < hi:
                merged.append(indices[j])
                j += 1
            indices[lo:hi] = merged

        merge_sort(0, len(nums))
        return counts
