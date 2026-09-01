import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_candies, run_maximum_candies
from .solution import Solution


class TestMaximumCandiesAllocatedToKChildren:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "candies, k, expected",
        [
            ([5, 8, 6], 3, 5),
            ([2, 5], 11, 0),
            ([1], 1, 1),
            ([1], 2, 0),
            ([10000000], 1, 10000000),
            ([10000000], 10000000, 1),
            ([10000000], 10000001, 0),
            ([4, 7, 5], 4, 3),
            ([1, 2, 3, 4, 5], 5, 2),
            ([8, 8, 8, 8], 8, 4),
            ([3, 3, 3], 10, 0),
            ([5, 6, 4, 11, 9], 6, 4),
            ([1000000, 1000000, 1000000, 1000000, 1000000], 5000000, 1),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1000000000000, 0),
            ([9999999, 9999999, 9999999, 9999999], 7, 4999999),
            ([10, 10, 10], 9, 3),
            ([6, 2, 9, 4, 1], 12, 1),
            ([10000000, 10000000, 10000000], 3000000, 10),
            ([34], 6, 5),
            ([18, 21, 18], 16, 3),
            ([25, 15, 12], 30, 1),
            ([48, 27], 17, 4),
        ],
    )
    def test_maximum_candies(self, candies: list[int], k: int, expected: int):
        result = run_maximum_candies(Solution, candies, k)
        assert_maximum_candies(result, expected)
