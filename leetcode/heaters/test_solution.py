import pytest

from leetcode_py import logged_test

from .helpers import assert_find_radius, run_find_radius
from .solution import Solution


class TestHeaters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "houses, heaters, expected",
        [
            ([1, 2, 3], [2], 1),
            ([1, 2, 3, 4], [1, 4], 1),
            ([1, 5], [2], 3),
            ([1], [1], 0),
            ([2], [1], 1),
            ([1, 2], [1, 4], 1),
            ([5], [1, 10], 4),
            ([1, 5, 10], [3, 7], 3),
            ([1, 2, 3, 5, 8, 13, 21], [2, 8, 21], 5),
            ([999999999, 1], [500000000], 499999999),
            ([3, 1, 2], [2], 1),
            ([1, 3, 5, 7], [2, 6], 1),
            ([1, 4, 9, 16, 25], [2, 8, 24], 8),
            ([10], [10], 0),
            ([1, 1000000000], [500000000], 500000000),
            ([7, 4, 9], [3], 6),
            ([1], [25, 22, 27, 11], 10),
            ([4], [15, 5, 29], 1),
            ([12], [11, 9], 1),
            ([12, 1, 22, 5, 5, 18], [28, 24, 4, 19], 7),
            ([15, 21, 3, 5], [13, 1, 27], 6),
            ([25, 13, 8, 12, 8, 30], [29, 2, 8, 27], 5),
        ],
    )
    def test_find_radius(self, houses: list[int], heaters: list[int], expected: int):
        result = run_find_radius(Solution, houses, heaters)
        assert_find_radius(result, expected)
