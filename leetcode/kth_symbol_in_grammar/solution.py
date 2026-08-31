class Solution:
    # Time: O(1)
    # Space: O(1)
    def kth_grammar(self, n: int, k: int) -> int:
        # kth symbol = parity of set bits in k - 1
        return (k - 1).bit_count() % 2
