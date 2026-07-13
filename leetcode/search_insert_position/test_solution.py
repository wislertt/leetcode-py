import pytest

from leetcode_py import logged_test

from .helpers import assert_search_insert, run_search_insert
from .solution import Solution


class TestTestSearchInsertPosition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 3, 5, 6], 7, 4),
            ([1, 3, 5, 6], 0, 0),
            ([1], 0, 0),
            ([1], 1, 0),
            ([1], 2, 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 10),
            ([-5, -3, -1, 0, 2, 4], -4, 1),
            ([-5, -3, -1, 0, 2, 4], -5, 0),
            ([10, 20, 30, 40, 50], 25, 2),
            ([1, 3, 5], 4, 2),
        ],
    )
    def test_search_insert(self, nums: list[int], target: int, expected: int):
        result = run_search_insert(Solution, nums, target)
        assert_search_insert(result, expected)
