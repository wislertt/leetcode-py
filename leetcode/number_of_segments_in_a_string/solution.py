class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_segments(self, s: str) -> int:
        count = 0
        in_segment = False
        for ch in s:
            if ch != " " and not in_segment:
                count += 1
                in_segment = True
            elif ch == " ":
                in_segment = False
        return count
