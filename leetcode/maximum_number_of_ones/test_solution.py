import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_number_of_ones, run_maximum_number_of_ones
from .solution import Solution


class TestMaximumNumberOfOnes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "width, height, side_length, max_ones, expected",
        [
            (3, 3, 2, 1, 4),
            (3, 3, 2, 2, 6),
            (1, 1, 1, 0, 0),
            (1, 1, 1, 1, 1),
            (2, 2, 2, 1, 1),
            (2, 2, 2, 4, 4),
            (3, 3, 1, 1, 9),
            (2, 3, 2, 2, 4),
            (5, 5, 2, 1, 9),
            (4, 5, 2, 2, 12),
            (7, 7, 3, 3, 21),
            (1, 100, 1, 1, 100),
            (100, 1, 1, 1, 100),
            (10, 10, 3, 0, 0),
            (100, 100, 10, 1, 100),
            (100, 100, 10, 50, 5000),
            (6, 7, 4, 8, 28),
            (20, 17, 5, 6, 96),
            (2, 2, 2, 0, 0),
            (9, 12, 4, 5, 42),
        ],
    )
    def test_maximum_number_of_ones(
        self, width: int, height: int, side_length: int, max_ones: int, expected: int
    ):
        result = run_maximum_number_of_ones(Solution, width, height, side_length, max_ones)
        assert_maximum_number_of_ones(result, expected)
