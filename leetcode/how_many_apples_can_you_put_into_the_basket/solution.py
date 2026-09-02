class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def max_number_of_apples(self, weight: list[int]) -> int:
        total = 0
        for count, w in enumerate(sorted(weight)):
            total += w
            if total > 5000:
                return count
        return len(weight)
