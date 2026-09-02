class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_recolors(self, blocks: str, k: int) -> int:
        whites = sum(1 for c in blocks[:k] if c == "W")
        best = whites
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                whites += 1
            if blocks[i - k] == "W":
                whites -= 1
            best = min(best, whites)
        return best
