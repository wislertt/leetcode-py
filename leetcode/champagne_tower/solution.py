class Solution:
    # Time: O(query_row^2)
    # Space: O(query_row)
    def champagne_tower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for _ in range(query_row):
            nxt = [0.0] * (len(row) + 1)
            for i, amount in enumerate(row):
                excess = max(0.0, amount - 1.0) / 2.0
                nxt[i] += excess
                nxt[i + 1] += excess
            row = nxt
        return min(1.0, row[query_glass])
