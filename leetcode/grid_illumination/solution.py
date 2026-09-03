class Solution:
    # Time: O(L + Q) where L = len(lamps), Q = len(queries) (9 turns per query)
    # Space: O(L)
    def grid_illumination(
        self, n: int, lamps: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        lit: set[tuple[int, int]] = set()
        for r, c in lamps:
            lit.add((r, c))
        rows: dict[int, int] = {}
        cols: dict[int, int] = {}
        diag: dict[int, int] = {}
        anti: dict[int, int] = {}
        for r, c in lit:
            rows[r] = rows.get(r, 0) + 1
            cols[c] = cols.get(c, 0) + 1
            diag[r - c] = diag.get(r - c, 0) + 1
            anti[r + c] = anti.get(r + c, 0) + 1

        result: list[int] = []
        for r, c in queries:
            is_lit = (
                rows.get(r, 0) > 0
                or cols.get(c, 0) > 0
                or diag.get(r - c, 0) > 0
                or anti.get(r + c, 0) > 0
            )
            result.append(1 if is_lit else 0)
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    lamp = (r + dr, c + dc)
                    if lamp in lit:
                        lit.remove(lamp)
                        rows[lamp[0]] -= 1
                        cols[lamp[1]] -= 1
                        diag[lamp[0] - lamp[1]] -= 1
                        anti[lamp[0] + lamp[1]] -= 1
        return result
