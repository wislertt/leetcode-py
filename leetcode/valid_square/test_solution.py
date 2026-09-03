import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_square, run_valid_square
from .solution import Solution


class TestValidSquare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "p1, p2, p3, p4, expected",
        [
            ([0, 0], [1, 1], [1, 0], [0, 1], True),
            ([0, 0], [1, 1], [1, 0], [0, 12], False),
            ([1, 0], [-1, 0], [0, 1], [0, -1], True),
            ([0, 0], [0, 0], [0, 0], [0, 0], False),
            ([0, 0], [1, 0], [0, 1], [1, 1], True),
            ([1, 1], [0, 0], [0, 1], [1, 0], True),
            ([0, 0], [0, 1], [1, 1], [2, 1], False),
            ([0, 0], [3, 0], [3, 3], [0, 3], True),
            ([0, 0], [1, 1], [1, 0], [0, 2], False),
            ([0, 0], [5, 0], [5, 5], [0, 5], True),
            ([0, 0], [0, 5], [0, 10], [0, 15], False),
            ([9999, 9999], [9999, 0], [0, 9999], [0, 0], True),
            ([-10000, -10000], [10000, -10000], [10000, 10000], [-10000, 10000], True),
            ([0, 0], [1, 2], [2, 1], [2, 2], False),
            ([2, 2], [2, 5], [5, 5], [5, 2], True),
        ],
    )
    def test_valid_square(
        self, p1: list[int], p2: list[int], p3: list[int], p4: list[int], expected: bool
    ):
        result = run_valid_square(Solution, p1, p2, p3, p4)
        assert_valid_square(result, expected)
