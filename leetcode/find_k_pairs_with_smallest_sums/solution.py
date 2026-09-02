import heapq


class Solution:
    # Time: O(k log min(k, len(nums1)))
    # Space: O(min(k, len(nums1)))
    def k_smallest_pairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        result: list[list[int]] = []
        heap: list[tuple[int, int, int]] = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result
