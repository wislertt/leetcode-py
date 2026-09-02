class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def reverse_pairs(self, nums: list[int]) -> int:
        def merge_sort(values: list[int]) -> tuple[list[int], int]:
            if len(values) <= 1:
                return values, 0
            mid = len(values) // 2
            left, left_pairs = merge_sort(values[:mid])
            right, right_pairs = merge_sort(values[mid:])
            pairs = left_pairs + right_pairs
            j = 0
            for x in left:
                while j < len(right) and x > 2 * right[j]:
                    j += 1
                pairs += j
            merged: list[int] = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, pairs

        _, total = merge_sort(nums)
        return total
