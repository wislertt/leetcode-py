class Solution:
    # Time: O(n * L) where L is the sequence length (10)
    # Space: O(n * L)
    def repeated_dna_sequences(self, s: str) -> list[str]:
        seen: set[str] = set()
        repeated: set[str] = set()
        for i in range(len(s) - 9):
            sequence = s[i : i + 10]
            if sequence in seen:
                repeated.add(sequence)
            seen.add(sequence)
        return list(repeated)
