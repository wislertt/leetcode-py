class Solution:
    def number_of_substrings(self, s: str) -> int:
        count = 0
        last = [-1, -1, -1]
        for i, ch in enumerate(s):
            last[ord(ch) - 97] = i
            count += min(last) + 1
        return count
