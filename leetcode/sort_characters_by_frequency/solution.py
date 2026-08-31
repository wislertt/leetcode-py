from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def frequency_sort(self, s: str) -> str:
        counts = Counter(s)
        buckets: list[list[str]] = [[] for _ in range(len(s) + 1)]
        for char, freq in counts.items():
            buckets[freq].append(char)

        parts: list[str] = []
        for freq in range(len(s), 0, -1):
            for char in buckets[freq]:
                parts.append(char * freq)
        return "".join(parts)
