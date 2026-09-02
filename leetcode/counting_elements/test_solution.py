import pytest

from leetcode_py import logged_test

from .helpers import assert_count_elements, run_count_elements
from .solution import Solution


class TestCountingElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2, 3], 2),
            ([1, 1, 3, 3, 5, 5, 7, 7], 0),
            ([1, 1, 2], 2),
            ([1, 3], 0),
            ([1], 0),
            ([0], 0),
            ([0, 1], 1),
            ([1000], 0),
            ([999, 1000], 1),
            ([1, 2, 2, 3], 3),
            ([1, 1, 2, 2], 2),
            ([7, 7, 7, 7, 7], 0),
            ([1, 2, 3, 4, 5], 4),
            ([10, 9, 8, 7, 6], 4),
            ([2, 9, 0, 1], 2),
            ([3, 1, 4, 1, 5, 9, 2, 6], 6),
            ([500, 501, 502, 499], 3),
            ([0, 0, 1, 1, 2, 2], 4),
            ([5, 4, 3, 2, 1, 1, 2, 3], 7),
            ([100, 101, 200, 201, 300], 2),
            ([6, 3], 0),
            ([10], 0),
            ([0, 8, 10, 1], 1),
            ([3], 0),
            ([8, 8], 0),
            ([15, 12, 14, 14, 12], 2),
        ],
    )
    def test_count_elements(self, arr: list[int], expected: int):
        result = run_count_elements(Solution, arr)
        assert_count_elements(result, expected)
