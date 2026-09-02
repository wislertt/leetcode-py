class Solution:
    # Time: O(n * L + 26^2 * S) where S is the largest group size
    # Space: O(n * L)
    def distinct_names(self, ideas: list[str]) -> int:
        groups: list[set[str]] = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord("a")].add(idea[1:])

        total = 0
        for a in range(26):
            for b in range(a + 1, 26):
                common = len(groups[a] & groups[b])
                total += 2 * (len(groups[a]) - common) * (len(groups[b]) - common)
        return total
