class Solution:
    # Time: O(volume * n)
    # Space: O(1) extra
    def pour_water(self, heights: list[int], volume: int, k: int) -> list[int]:
        n = len(heights)
        for _ in range(volume):
            best = k
            for d in (-1, 1):
                i = best = k
                while 0 <= i + d < n and heights[i + d] <= heights[i]:
                    if heights[i + d] < heights[best]:
                        best = i + d
                    i += d
                if best != k:
                    break
            heights[best] += 1
        return heights
