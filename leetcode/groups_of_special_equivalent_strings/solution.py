class Solution:
    # Time: O(n * l log l)
    # Space: O(n * l)
    def num_special_equivalent_groups(self, words: list[str]) -> int:
        signatures = {("".join(sorted(word[0::2])), "".join(sorted(word[1::2]))) for word in words}
        return len(signatures)
