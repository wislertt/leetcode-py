import pytest

from leetcode_py import logged_test

from .helpers import assert_min_moves_to_seat, run_min_moves_to_seat
from .solution import Solution


class TestMinimumNumberOfMovesToSeatEveryone:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "seats, students, expected",
        [
            ([3, 1, 5], [2, 7, 4], 4),
            ([4, 1, 5, 9], [1, 3, 2, 6], 7),
            ([2, 2, 6, 6], [1, 3, 2, 6], 4),
            ([1], [1], 0),
            ([1], [100], 99),
            ([100], [1], 99),
            ([2, 2], [2, 2], 0),
            ([1, 2, 3], [1, 2, 3], 0),
            ([1, 4], [2, 3], 2),
            ([3, 20], [20, 3], 0),
            ([12, 14, 19, 19, 12], [19, 14, 12, 12, 19], 0),
            ([2, 5, 1, 6], [1, 6, 2, 5], 0),
            ([5, 1, 3, 7], [2, 6, 4, 8], 4),
            ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5),
            ([10, 20, 30], [1, 2, 3], 54),
            ([100, 1, 50], [50, 100, 1], 0),
            ([7, 4, 9, 1], [5, 8, 2, 10], 4),
            ([3, 3, 3], [1, 5, 3], 4),
        ],
    )
    def test_min_moves_to_seat(self, seats: list[int], students: list[int], expected: int):
        result = run_min_moves_to_seat(Solution, seats, students)
        assert_min_moves_to_seat(result, expected)
