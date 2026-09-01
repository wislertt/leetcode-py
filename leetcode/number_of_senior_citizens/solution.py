class Solution:
    # Time: O(n)
    # Space: O(1)
    def count_seniors(self, details: list[str]) -> int:
        return sum(int(detail[11:13]) > 60 for detail in details)
