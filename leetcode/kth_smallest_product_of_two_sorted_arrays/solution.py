from bisect import bisect_left, bisect_right


class Solution:
    # Time: O((len(nums1) + len(nums2)) * log(len(nums2)) * log(max_product))
    # Space: O(1)
    def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count_at_most(target: int) -> int:
            total = 0
            for a in nums1:
                if a == 0:
                    if target >= 0:
                        total += len(nums2)
                elif a > 0:
                    total += bisect_right(nums2, target // a)
                else:
                    total += len(nums2) - bisect_left(nums2, -(target // -a))
            return total

        low, high = -(10**10), 10**10
        while low < high:
            mid = (low + high) // 2
            if count_at_most(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low
