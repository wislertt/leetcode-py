class Solution:
    # Time: O(width * height)
    # Space: O(sideLength^2)
    def maximum_number_of_ones(
        self, width: int, height: int, side_length: int, max_ones: int
    ) -> int:
        x = side_length
        counts = [0] * (x * x)
        for i in range(width):
            for j in range(height):
                counts[(i % x) * x + (j % x)] += 1
        counts.sort(reverse=True)
        return sum(counts[:max_ones])
