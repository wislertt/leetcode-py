class Solution:
    # Time: O(n * m^2)
    # Space: O(1)
    def count_prefix_suffix_pairs(self, words: list[str]) -> int:
        count = 0
        for i, prefix in enumerate(words):
            for suffix in words[i + 1 :]:
                if suffix.startswith(prefix) and suffix.endswith(prefix):
                    count += 1
        return count
