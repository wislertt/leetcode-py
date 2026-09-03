class Solution:
    # Time: O(n * w^2)
    # Space: O(n * w)
    def min_deletion_size(self, strs: list[str]) -> int:
        keep = [""] * len(strs)
        deleted = 0
        for j in range(len(strs[0])):
            candidate = [row + s[j] for row, s in zip(keep, strs, strict=True)]
            if all(candidate[i] <= candidate[i + 1] for i in range(len(candidate) - 1)):
                keep = candidate
            else:
                deleted += 1
        return deleted
