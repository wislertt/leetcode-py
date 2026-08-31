class Solution:
    # Time: O(n!) bounded by distinct-letter tree size
    # Space: O(n)
    def num_tile_possibilities(self, tiles: str) -> int:
        counts: dict[str, int] = {}
        for ch in tiles:
            counts[ch] = counts.get(ch, 0) + 1

        def dfs() -> int:
            total = 0
            for ch in counts:
                if counts[ch] == 0:
                    continue
                counts[ch] -= 1
                total += 1 + dfs()
                counts[ch] += 1
            return total

        return dfs()
