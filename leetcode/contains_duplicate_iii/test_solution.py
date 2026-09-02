import pytest

from leetcode_py import logged_test

from .helpers import assert_contains_nearby_almost_duplicate, run_contains_nearby_almost_duplicate
from .solution import Solution


class TestContainsDuplicateIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, index_diff, value_diff, expected",
        [
            ([1, 2, 3, 1], 3, 0, True),
            ([1, 5, 9, 1, 5, 9], 2, 3, False),
            ([1, 2, 3, 1], 2, 0, False),
            ([1, 1], 1, 0, True),
            ([1, 2], 1, 1, True),
            ([1, 2], 1, 0, False),
            ([1, 3, 1], 1, 1, False),
            ([1, 3, 1], 2, 1, True),
            ([1, 2, 3, 4, 5], 3, 1, True),
            ([1, 5, 9, 13], 3, 3, False),
            ([-1, -1], 1, 0, True),
            ([1000000000, -1000000000], 1, 2000000000, True),
            ([1000000000, -1000000000], 1, 1999999999, False),
            ([4, 2, 3, 1], 2, 1, True),
            ([2, 1], 1, 0, False),
            ([1, 2, 3, 4], 1, 0, False),
            ([5, 5, 5, 5], 3, 0, True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 0, False),
            ([-3, 4, -2], 3, 5, True),
            ([5, -4, 0, -3, 5], 2, 5, True),
            ([2, 8, -4, -10], 1, 1, False),
            ([6, -1], 2, 0, False),
            ([-8, -8, -5, -10], 2, 2, True),
            ([-8, 8, 10, 6], 2, 1, False),
            ([-7, -10], 1, 5, True),
            ([9, 5, 5, -2], 4, 1, True),
        ],
    )
    def test_contains_nearby_almost_duplicate(
        self, nums: list[int], index_diff: int, value_diff: int, expected: bool
    ):
        result = run_contains_nearby_almost_duplicate(Solution, nums, index_diff, value_diff)
        assert_contains_nearby_almost_duplicate(result, expected)
