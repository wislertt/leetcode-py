import pytest

from leetcode_py import logged_test

from .helpers import assert_pancake_sort, run_pancake_sort
from .solution import Solution


class TestPancakeSorting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([2, 3, 1], [1, 2, 3]),
            ([3, 1, 2], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([3, 2, 4, 1], [1, 2, 3, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([1, 4, 2, 3], [1, 2, 3, 4]),
            ([2, 1, 4, 3], [1, 2, 3, 4]),
            ([4, 1, 3, 2], [1, 2, 3, 4]),
            ([5, 1, 2, 3, 4], [1, 2, 3, 4, 5]),
            ([2, 4, 1, 5, 3], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 5, 4], [1, 2, 3, 4, 5]),
            ([3, 1, 2, 6, 4, 5], [1, 2, 3, 4, 5, 6]),
            ([6, 2, 4, 1, 5, 3], [1, 2, 3, 4, 5, 6]),
            ([7, 1, 5, 3, 6, 4, 2], [1, 2, 3, 4, 5, 6, 7]),
            ([4, 6, 2, 7, 1, 5, 3], [1, 2, 3, 4, 5, 6, 7]),
            ([4, 2, 7, 3, 1, 5, 6], [1, 2, 3, 4, 5, 6, 7]),
            ([1, 4, 3, 2], [1, 2, 3, 4]),
            ([1, 3, 4, 2, 6, 7, 5], [1, 2, 3, 4, 5, 6, 7]),
            ([6, 3, 5, 1, 7, 4, 2, 8], [1, 2, 3, 4, 5, 6, 7, 8]),
        ],
    )
    def test_pancake_sort(self, arr: list[int], expected: list[int]):
        result = run_pancake_sort(Solution, arr)
        assert_pancake_sort(result, arr, expected)
