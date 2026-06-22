class Solution:
    # Time: O(n)
    # Space: O(1) — alphabet bounded to 26
    def partition_labels(self, s: str) -> list[int]:
        last_occurrence: dict[str, int] = {char: idx for idx, char in enumerate(s)}
        partitions: list[int] = []
        start, end = 0, 0
        for idx, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if idx == end:
                partitions.append(idx - start + 1)
                start = idx + 1
        return partitions
