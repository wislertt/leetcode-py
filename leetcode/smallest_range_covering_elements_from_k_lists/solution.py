import heapq


class Solution:
    # Min-heap holds current element from each list. Range = [heap_min, current_max].
    # Repeatedly pop min and advance that list; track smallest range seen.
    # Time: O(n log k) where n = total elements, k = number of lists
    # Space: O(k)
    def smallest_range(self, nums: list[list[int]]) -> list[int]:
        heap: list[tuple[int, int, int]] = []
        current_max = -(10**5) - 1
        for list_idx, lst in enumerate(nums):
            val = lst[0]
            heapq.heappush(heap, (val, list_idx, 0))
            current_max = max(current_max, val)

        best_start, best_end = -(10**5) - 1, 10**5 + 1

        while heap:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            # Candidate range covers all lists: [min_val, current_max]
            if current_max - min_val < best_end - best_start:
                best_start, best_end = min_val, current_max
            # Advance the list that supplied the min; stop if exhausted
            if elem_idx + 1 == len(nums[list_idx]):
                break
            next_val = nums[list_idx][elem_idx + 1]
            current_max = max(current_max, next_val)
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

        return [best_start, best_end]
