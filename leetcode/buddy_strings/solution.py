class Solution:
    # Time: O(n)
    # Space: O(1)
    def buddy_strings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diffs = [i for i, (a, b) in enumerate(zip(s, goal, strict=True)) if a != b]
        if len(diffs) != 2:
            return False
        i, j = diffs
        return s[i] == goal[j] and s[j] == goal[i]
