import pytest

from leetcode_py import logged_test

from .helpers import assert_get_index, run_get_index
from .solution import Solution


class TestFindTheIndexOfTheLargeInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([7, 7, 7, 7, 10, 7, 7, 7], 4),
            ([6, 6, 12], 2),
            ([1, 2], 1),
            ([3, 1], 0),
            ([5, 5, 5, 9], 3),
            ([9, 5, 5, 5], 0),
            ([4, 4, 7, 4], 2),
            ([2, 2, 2, 2, 2, 2, 8, 2], 6),
            ([100, 1], 0),
            ([1, 100], 1),
            ([53, 92, 53, 53], 1),
            ([60, 69, 60, 60, 60, 60, 60, 60], 1),
            ([40, 40, 40, 40, 40, 40, 88, 40], 6),
            ([60, 60, 60, 72, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60], 3),
            ([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 34, 5, 5, 5, 5], 11),
            ([17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 49, 17, 17, 17, 17], 11),
            ([4, 4, 4, 77, 4, 4, 4, 4], 3),
            ([83, 88, 83, 83, 83, 83, 83, 83], 1),
            ([89, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84], 0),
            ([30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 42, 30, 30, 30, 30], 11),
            ([81, 81, 81, 81, 81, 81, 81, 81, 100, 81, 81, 81, 81, 81, 81, 81], 8),
        ],
    )
    def test_get_index(self, arr: list[int], expected: int):
        result = run_get_index(Solution, arr)
        assert_get_index(result, expected)
