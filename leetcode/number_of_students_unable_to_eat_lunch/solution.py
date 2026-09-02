class Solution:
    # Time: O(n + m) where n = len(students), m = len(sandwiches)
    # Space: O(1) - only two counters
    def count_students(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [0, 0]
        for pref in students:
            counts[pref] += 1
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
        return counts[0] + counts[1]
