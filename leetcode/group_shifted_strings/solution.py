from collections import defaultdict


class Solution:
    # Time: O(L) where L is total length of all strings
    # Space: O(L)
    def group_strings(self, strings: list[str]) -> list[list[str]]:
        groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)
        for s in strings:
            shift = ord(s[0]) - ord("a")
            key = tuple((ord(c) - ord("a") - shift) % 26 for c in s)
            groups[key].append(s)
        return list(groups.values())
