class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted copies
    def min_moves_to_seat(self, seats: list[int], students: list[int]) -> int:
        return sum(
            abs(seat - student)
            for seat, student in zip(sorted(seats), sorted(students), strict=True)
        )
