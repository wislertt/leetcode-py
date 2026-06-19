import pytest

from leetcode_py import logged_test

from .helpers import assert_plus_one, run_plus_one
from .solution import Solution


class TestPlusOne:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "digits, expected",
        [
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),
            ([9], [1, 0]),
            ([0], [1]),
            ([1, 0, 0, 0], [1, 0, 0, 1]),
            ([9, 9], [1, 0, 0]),
            ([9, 9, 9], [1, 0, 0, 0]),
            ([8, 9, 9, 9], [9, 0, 0, 0]),
            ([2], [3]),
            ([1, 9], [2, 0]),
            ([7, 7, 7], [7, 7, 8]),
            ([5, 9, 9], [6, 0, 0]),
            ([1, 2, 9], [1, 3, 0]),
            ([6, 1, 4, 9], [6, 1, 5, 0]),
        ],
    )
    def test_plus_one(self, digits: list[int], expected: list[int]):
        result = run_plus_one(Solution, digits)
        assert_plus_one(result, expected)
