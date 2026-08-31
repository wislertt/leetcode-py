import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_values, run_largest_values
from .solution import Solution


class TestFindLargestValueInEachTreeRow:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 3, 2, 5, 3, None, 9], [1, 3, 9]),
            ([1, 2, 3], [1, 3]),
            ([], []),
            ([1], [1]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),
            ([1, None, 2], [1, 2]),
            ([1, 2, None], [1, 2]),
            ([-10, -20, -5], [-10, -5]),
            ([5, 4, 6, 1, 3, 7, 9], [5, 6, 9]),
            ([1, 2, 3, None, None, 4, 5], [1, 3, 5]),
            ([100], [100]),
            ([3, 9, 20, None, None, 15, 7], [3, 20, 15]),
            ([-2147483648, 2147483647], [-2147483648, 2147483647]),
            ([7, 3, 9, 1, 4, None, 11], [7, 9, 11]),
            ([1, 1, 1, 1], [1, 1, 1]),
        ],
    )
    def test_largest_values(self, root_list: list[int | None], expected: list[int]):
        result = run_largest_values(Solution, root_list)
        assert_largest_values(result, expected)
