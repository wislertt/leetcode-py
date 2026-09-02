import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_element, run_maximum_element
from .solution import Solution


class TestMaximumElementAfterDecreasingAndRearranging:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 2, 1, 2, 1], 2),
            ([100, 1, 1000], 3),
            ([1, 2, 3, 4, 5], 5),
            ([5], 1),
            ([1], 1),
            ([1000000000], 1),
            ([1, 1000000000], 2),
            ([2, 1], 2),
            ([1, 1, 1, 1], 1),
            ([3, 3, 3], 3),
            ([73, 98, 9], 3),
            ([2, 2, 1, 2, 1, 2], 2),
            ([10, 1, 1, 1, 1], 2),
            ([4, 5, 6, 7, 1, 2, 3], 7),
            ([4, 5, 3, 2, 5, 4, 1, 5], 5),
            ([1, 1, 2, 2, 2], 2),
            ([818170495, 927972824, 321022891, 960882592, 907895290, 849987153], 6),
            ([10, 8, 10, 8, 2, 8, 2], 7),
        ],
    )
    def test_maximum_element(self, arr: list[int], expected: int):
        result = run_maximum_element(Solution, arr)
        assert_maximum_element(result, expected)
