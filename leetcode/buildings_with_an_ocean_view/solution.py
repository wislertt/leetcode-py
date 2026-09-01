class Solution:
    # Time: O(n)
    # Space: O(1) excluding the output list
    def find_buildings(self, heights: list[int]) -> list[int]:
        result: list[int] = []
        max_right = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_right:
                result.append(i)
                max_right = heights[i]

        return result[::-1]
