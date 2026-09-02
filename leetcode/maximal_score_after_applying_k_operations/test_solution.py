import pytest

from leetcode_py import logged_test

from .helpers import assert_max_kelements, run_max_kelements
from .solution import Solution


class TestMaximalScoreAfterApplyingKOperations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([10, 10, 10, 10, 10], 5, 50),
            ([1, 10, 3, 3, 3], 3, 17),
            ([1], 1, 1),
            ([1], 3, 3),
            ([5], 2, 7),
            ([9], 3, 13),
            ([1, 2], 2, 3),
            ([1, 2, 3], 3, 6),
            ([3, 3, 3], 4, 10),
            ([1000000000], 2, 1333333334),
            ([1000000000, 1], 3, 1444444446),
            ([6, 1, 9], 5, 21),
            ([2, 8, 4, 16], 6, 39),
            ([7, 5, 3, 1], 7, 22),
            ([1000000000, 1000000000, 1000000000], 4, 3333333334),
            ([1, 1, 1, 1, 1], 10, 10),
            ([4, 4, 4], 8, 20),
        ],
    )
    def test_max_kelements(self, nums: list[int], k: int, expected: int):
        result = run_max_kelements(Solution, nums, k)
        assert_max_kelements(result, expected)
