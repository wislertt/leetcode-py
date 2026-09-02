import pytest

from leetcode_py import logged_test

from .helpers import assert_plus_one, run_plus_one
from .solution import Solution


class TestPlusOneLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, expected_vals",
        [
            ([1, 2, 3], [1, 2, 4]),
            ([0], [1]),
            ([9], [1, 0]),
            ([9, 9, 9], [1, 0, 0, 0]),
            ([1, 9, 9], [2, 0, 0]),
            ([1, 0, 0], [1, 0, 1]),
            ([7, 8, 9, 9], [7, 9, 0, 0]),
            ([9, 8, 7], [9, 8, 8]),
            ([1], [2]),
            ([5], [6]),
            ([9, 9, 1, 9, 9], [9, 9, 2, 0, 0]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9, 0]),
            ([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            ([8, 9], [9, 0]),
            ([2, 4, 9], [2, 5, 0]),
            ([1, 8, 9], [1, 9, 0]),
        ],
    )
    def test_plus_one(self, head_vals: list[int], expected_vals: list[int]):
        result = run_plus_one(Solution, head_vals)
        assert_plus_one(result, expected_vals)
