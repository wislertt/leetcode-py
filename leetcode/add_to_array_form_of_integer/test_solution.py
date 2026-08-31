import pytest

from leetcode_py import logged_test

from .helpers import assert_add_to_array_form, run_add_to_array_form
from .solution import Solution


class TestAddToArrayFormOfInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, k, expected",
        [
            ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
            ([2, 7, 4], 181, [4, 5, 5]),
            ([2, 1, 5], 806, [1, 0, 2, 1]),
            ([0], 1, [1]),
            ([0], 1000, [1, 0, 0, 0]),
            ([9, 9, 9], 1, [1, 0, 0, 0]),
            ([1], 9999, [1, 0, 0, 0, 0]),
            ([5, 5, 5], 555, [1, 1, 1, 0]),
            ([9], 9, [1, 8]),
            ([1, 0, 0, 0, 0, 0, 0, 0], 1, [1, 0, 0, 0, 0, 0, 0, 1]),
            ([3, 8, 1], 619, [1, 0, 0, 0]),
            ([7], 993, [1, 0, 0, 0]),
        ],
    )
    def test_add_to_array_form(self, num: list[int], k: int, expected: list[int]):
        result = run_add_to_array_form(Solution, num, k)
        assert_add_to_array_form(result, expected)
