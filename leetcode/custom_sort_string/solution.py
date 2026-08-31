class Solution:
    # Time: O(len(s) log len(s))
    # Space: O(len(s))
    def custom_sort_string(self, order: str, s: str) -> str:
        rank = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda c: rank.get(c, 26)))
