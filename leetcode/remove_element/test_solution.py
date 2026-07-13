import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_element, run_remove_element
from .solution import Solution


class TestTestRemoveElement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, val, expected",
        [
            ([3, 2, 2, 3], 3, (2, [2, 2])),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, (5, [0, 0, 1, 3, 4])),
            ([], 1, (0, [])),
            ([1], 1, (0, [])),
            ([1], 2, (1, [1])),
            ([2, 2, 2, 2], 2, (0, [])),
            ([1, 2, 3, 4, 5], 6, (5, [1, 2, 3, 4, 5])),
            ([4, 4, 4, 4], 4, (0, [])),
            ([0, 1, 2, 3, 4, 5], 0, (5, [1, 2, 3, 4, 5])),
            ([5, 5, 5, 1, 5], 5, (1, [1])),
            ([1, 2, 3, 4, 5], 3, (4, [1, 2, 4, 5])),
            ([50, 50, 50], 50, (0, [])),
        ],
    )
    def test_remove_element(self, nums: list[int], val: int, expected: tuple[int, list[int]]):
        result = run_remove_element(Solution, nums, val)
        assert_remove_element(result, expected)
