class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def count_range_sum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        def sort_count(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
            mid = (left + right) // 2
            count = sort_count(left, mid) + sort_count(mid, right)
            low_part = sorted(prefix[left:mid])
            high_part = sorted(prefix[mid:right])
            start = end = 0
            for value in low_part:
                while start < len(high_part) and high_part[start] - value < lower:
                    start += 1
                while end < len(high_part) and high_part[end] - value <= upper:
                    end += 1
                count += end - start
            merged: list[int] = []
            i = j = 0
            while i < len(low_part) and j < len(high_part):
                if low_part[i] <= high_part[j]:
                    merged.append(low_part[i])
                    i += 1
                else:
                    merged.append(high_part[j])
                    j += 1
            merged.extend(low_part[i:])
            merged.extend(high_part[j:])
            prefix[left:right] = merged
            return count

        return sort_count(0, len(prefix))
