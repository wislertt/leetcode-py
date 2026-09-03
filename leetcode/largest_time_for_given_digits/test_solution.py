import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_time_from_digits, run_largest_time_from_digits
from .solution import Solution


class TestLargestTimeForGivenDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2, 3, 4], "23:41"),
            ([5, 5, 5, 5], ""),
            ([0, 0, 0, 0], "00:00"),
            ([2, 3, 5, 9], "23:59"),
            ([1, 9, 9, 9], ""),
            ([2, 4, 6, 0], "20:46"),
            ([9, 5, 3, 1], "19:53"),
            ([6, 6, 6, 6], ""),
            ([2, 9, 9, 4], ""),
            ([1, 0, 0, 0], "10:00"),
            ([4, 7, 2, 3], "23:47"),
            ([0, 6, 9, 1], "19:06"),
            ([8, 3, 5, 1], "18:53"),
            ([2, 0, 6, 6], "06:26"),
            ([7, 9, 9, 1], ""),
            ([5, 5, 5, 4], ""),
            ([9, 4, 7, 8], ""),
            ([9, 5, 0, 2], "20:59"),
            ([4, 0, 6, 1], "16:40"),
            ([3, 6, 2, 7], ""),
            ([4, 0, 8, 1], "18:40"),
        ],
    )
    def test_largest_time_from_digits(self, arr: list[int], expected: str):
        result = run_largest_time_from_digits(Solution, arr)
        assert_largest_time_from_digits(result, expected)
