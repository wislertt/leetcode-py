class Solution:
    # Time: O(1)
    # Space: O(1)
    def distribute_candies(self, n: int, limit: int) -> int:
        def capped_ways(total: int) -> int:
            # Ways for 3 non-negative parts summing to `total`, ignoring the cap:
            # C(total + 2, 2); 0 when no composition exists.
            return (total + 2) * (total + 1) // 2 if total >= 0 else 0

        return (
            capped_ways(n)
            - 3 * capped_ways(n - (limit + 1))
            + 3 * capped_ways(n - 2 * (limit + 1))
            - capped_ways(n - 3 * (limit + 1))
        )
