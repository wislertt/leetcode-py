import pytest

from leetcode_py import logged_test

from .helpers import assert_tallest_billboard, run_tallest_billboard
from .solution import Solution


class TestTallestBillboard:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rods, expected",
        [
            ([1, 2, 3, 6], 6),
            ([1, 2, 3, 4, 5, 6], 10),
            ([1, 2], 0),
            ([1], 0),
            ([2, 2], 2),
            ([1, 1], 1),
            ([1, 2, 3], 3),
            ([1, 2, 4], 0),
            ([3, 3, 3, 3], 6),
            ([1, 1, 1, 1], 2),
            ([5, 5, 5, 5, 5], 10),
            ([1, 2, 3, 4, 5], 7),
            ([10, 10], 10),
            ([1000, 1000], 1000),
            ([1, 2, 3, 4, 5, 6, 7], 14),
            ([1, 1, 1, 1, 1, 1, 1, 1], 4),
            ([2, 3, 5, 7], 7),
            ([1, 3, 4, 7, 10], 11),
            ([5, 1, 2, 6, 3], 8),
            ([6, 6, 6], 6),
            ([1, 1000, 999, 2, 998], 1001),
            ([20, 20, 20, 20, 20, 20, 20, 20], 80),
        ],
    )
    def test_tallest_billboard(self, rods: list[int], expected: int):
        result = run_tallest_billboard(Solution, rods)
        assert_tallest_billboard(result, expected)
