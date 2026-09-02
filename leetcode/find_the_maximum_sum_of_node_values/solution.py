class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def maximum_value_sum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        # A tree lets any even-sized set of nodes be XORed with k (each edge op
        # toggles two endpoints; paths transfer a toggle and cancel out).
        # So maximize the sum of gains (x ^ k) - x over an even count of nodes.
        del edges
        total = sum(nums)
        gains = sorted(((x ^ k) - x for x in nums), reverse=True)
        for i in range(0, len(gains) - 1, 2):
            pair = gains[i] + gains[i + 1]
            if pair <= 0:
                break
            total += pair
        return total
