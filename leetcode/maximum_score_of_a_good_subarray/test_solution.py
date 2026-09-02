import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_score, run_maximum_score
from .solution import Solution


class TestMaximumScoreOfAGoodSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 4, 3, 7, 4, 5], 3, 15),
            ([5, 5, 4, 5, 4, 1, 1, 1], 0, 20),
            ([1], 0, 1),
            ([7], 0, 7),
            ([2, 2], 0, 4),
            ([1, 2], 0, 2),
            ([1, 2], 1, 2),
            ([3, 1, 3], 1, 3),
            ([9, 1, 1, 9], 1, 4),
            ([10, 8, 8, 10], 1, 32),
            ([4, 5, 6, 7], 2, 16),
            ([20000, 20000, 20000, 20000, 20000, 20000], 3, 120000),
            ([1, 20000, 1], 1, 20000),
            ([6, 3, 4, 2, 5, 1, 6], 3, 10),
            ([5, 4, 3, 2, 1], 0, 9),
            ([1, 2, 3, 4, 5], 4, 9),
            ([16774], 0, 16774),
            ([325], 0, 325),
            ([2751, 11173, 18477, 1688], 3, 6752),
            ([2128, 10712, 6408, 13633, 3164], 2, 19224),
        ],
    )
    def test_maximum_score(self, nums: list[int], k: int, expected: int):
        result = run_maximum_score(Solution, nums, k)
        assert_maximum_score(result, expected)
