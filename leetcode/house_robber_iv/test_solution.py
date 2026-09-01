import pytest

from leetcode_py import logged_test

from .helpers import assert_min_capability, run_min_capability
from .solution import Solution


class TestHouseRobberIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([2, 3, 5, 9], 2, 5),
            ([2, 7, 9, 3, 1], 2, 2),
            ([1], 1, 1),
            ([5], 1, 5),
            ([1, 2], 1, 1),
            ([2, 1], 1, 1),
            ([9, 1], 1, 1),
            ([4, 3, 2, 1], 2, 3),
            ([1, 2, 3, 4, 5], 3, 5),
            ([7, 17, 4, 2, 9, 1], 2, 2),
            ([1, 1, 1, 1, 1], 3, 1),
            ([2, 3, 5, 9], 1, 2),
            ([1000000000, 1, 1000000000], 2, 1000000000),
            ([9, 5, 14, 11, 8, 6, 17, 4], 3, 6),
            ([19], 1, 19),
            ([12], 1, 12),
            ([4, 13, 3, 9, 14, 6, 8, 17, 17], 3, 6),
            ([16, 9, 16, 3, 7, 14, 4, 19, 10], 3, 9),
            ([17, 1, 6, 6, 4, 2, 3, 18], 3, 4),
            ([7, 14, 17], 2, 17),
            ([13, 2, 13, 9, 7, 16], 2, 7),
            ([1, 20, 19, 16, 9, 15, 9, 6], 1, 1),
            ([20], 1, 20),
        ],
    )
    def test_min_capability(self, nums: list[int], k: int, expected: int):
        result = run_min_capability(Solution, nums, k)
        assert_min_capability(result, expected)
