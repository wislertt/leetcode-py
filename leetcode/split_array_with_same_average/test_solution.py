import pytest

from leetcode_py import logged_test

from .helpers import assert_split_array_same_average, run_split_array_same_average
from .solution import Solution


class TestSplitArrayWithSameAverage:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8], True),
            ([3, 1], False),
            ([1], False),
            ([0], False),
            ([1, 2], False),
            ([2, 2], True),
            ([0, 0, 0], True),
            ([1, 3], False),
            ([6, 8, 18, 3, 1], False),
            ([0, 13, 28, 8, 6, 7, 0, 8, 7, 6], False),
            ([10, 10, 10, 10], True),
            ([1, 2, 3, 4, 5], True),
            ([5, 5, 5, 5, 5, 5], True),
            ([2, 0, 5, 6, 16, 12, 15, 12, 4], True),
            ([84, 44, 32, 62, 50, 25, 75, 8, 23, 80, 19, 39, 63, 52, 72, 54], True),
            (
                [
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                ],
                True,
            ),
        ],
    )
    def test_split_array_same_average(self, nums: list[int], expected: bool):
        result = run_split_array_same_average(Solution, nums)
        assert_split_array_same_average(result, expected)
