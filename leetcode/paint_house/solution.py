class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_cost(self, costs: list[list[int]]) -> int:
        red = blue = green = 0
        for r, b, g in costs:
            red, blue, green = (
                min(blue, green) + r,
                min(red, green) + b,
                min(red, blue) + g,
            )
        return min(red, blue, green)
