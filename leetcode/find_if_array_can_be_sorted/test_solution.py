import pytest

from leetcode_py import logged_test

from .helpers import assert_can_sort_array, run_can_sort_array
from .solution import Solution


class TestFindIfArrayCanBeSorted:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([8, 4, 2, 30, 15], True),
            ([1, 2, 3, 4, 5], True),
            ([3, 16, 8, 4, 2], False),
            ([1], True),
            ([2, 1], True),
            ([3, 1], False),
            ([4, 8, 2], True),
            ([5, 4, 2, 1, 3], False),
            ([256, 1], True),
            ([16, 8, 1], True),
            ([7, 11, 3], False),
            ([10, 3, 5, 6], True),
            ([2, 4, 1, 8], True),
            ([100, 64, 32, 8], False),
            ([96, 72, 35], False),
            ([197, 152, 37, 4], False),
            ([132, 235, 113, 103], False),
            ([161, 136], False),
        ],
    )
    def test_can_sort_array(self, nums: list[int], expected: bool):
        result = run_can_sort_array(Solution, nums)
        assert_can_sort_array(result, expected)
