import pytest

from leetcode_py import logged_test

from .helpers import assert_transform_array, run_transform_array
from .solution import Solution


class TestArrayTransformation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([6, 2, 3, 4], [6, 3, 3, 4]),
            ([1, 6, 3, 4, 3, 5], [1, 4, 4, 4, 4, 5]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [3, 2, 1]),
            ([2, 1, 2], [2, 2, 2]),
            ([2, 3, 2], [2, 2, 2]),
            ([1, 5, 1, 5, 1], [1, 3, 3, 3, 1]),
            ([2, 2, 2, 2], [2, 2, 2, 2]),
            ([1, 100, 1], [1, 1, 1]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([9, 1, 9, 1, 9], [9, 5, 5, 5, 9]),
            ([10, 4, 4, 10], [10, 4, 4, 10]),
            ([5, 1, 5, 1, 5, 1, 5], [5, 3, 3, 3, 3, 3, 5]),
            ([1, 9, 1, 9, 1, 9, 1, 9, 1], [1, 5, 5, 5, 5, 5, 5, 5, 1]),
            ([4, 1, 4, 1, 4], [4, 3, 3, 3, 4]),
            ([7, 3, 7, 3, 7, 3, 7], [7, 5, 5, 5, 5, 5, 7]),
            ([6, 1, 7, 9, 8, 5, 3, 9, 2, 1, 1], [6, 6, 7, 8, 8, 5, 5, 5, 2, 1, 1]),
            ([6, 8, 2, 9, 4, 5, 2], [6, 6, 6, 5, 5, 4, 2]),
            ([8, 8, 5, 6, 2, 2, 7], [8, 8, 6, 5, 2, 2, 7]),
            ([5, 7, 8, 3], [5, 7, 7, 3]),
            ([2, 3, 1, 6, 2, 5], [2, 2, 2, 4, 4, 5]),
            ([2, 2, 8, 1, 3, 5, 4, 4, 5, 8, 2], [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 2]),
            ([3, 7, 7, 8, 7, 3], [3, 7, 7, 7, 7, 3]),
            ([9, 2, 7], [9, 7, 7]),
            ([7, 7, 3, 9, 4], [7, 7, 6, 6, 4]),
            ([4, 2, 4, 5, 9, 2, 2, 8], [4, 4, 4, 5, 5, 2, 2, 8]),
        ],
    )
    def test_transform_array(self, arr: list[int], expected: list[int]):
        result = run_transform_array(Solution, arr)
        assert_transform_array(result, expected)
