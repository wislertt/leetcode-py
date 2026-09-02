class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def number_of_beams(self, bank: list[str]) -> int:
        total = 0
        prev = 0
        for row in bank:
            count = row.count("1")
            if count:
                total += prev * count
                prev = count
        return total
