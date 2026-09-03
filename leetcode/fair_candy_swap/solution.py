class Solution:
    # Time: O(n + m)
    # Space: O(m)
    def fair_candy_swap(self, alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
        delta = (sum(alice_sizes) - sum(bob_sizes)) // 2
        bob_set = set(bob_sizes)
        for x in alice_sizes:
            y = x - delta
            if y in bob_set:
                return [x, y]
        return []  # unreachable: a valid answer is guaranteed
