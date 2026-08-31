class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copy
    def find_longest_chain(self, pairs: list[list[int]]) -> int:
        count = 0
        chain_end = float("-inf")
        for left, right in sorted(pairs, key=lambda pair: pair[1]):
            if left > chain_end:
                count += 1
                chain_end = right
        return count
