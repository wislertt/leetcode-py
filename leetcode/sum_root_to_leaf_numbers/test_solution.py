import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_numbers, run_sum_numbers
from .solution import Solution


class TestSumRootToLeafNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3], 25),
            ([4, 9, 0, 5, 1], 1026),
            ([0], 0),
            ([5], 5),
            ([9], 9),
            ([1, 2], 12),
            ([1, None, 3], 13),
            ([0, 0, 0], 0),
            ([1, 0, 0], 20),
            ([9, 9, 9, 9, 9, 9, 9], 3996),
            ([9, 9, 9, 9, None, None, 9], 1998),
            ([1, 2, 3, 4, 5, 6, 7], 522),
            ([2, 1, None, None, 3], 213),
            ([1, None, 2, None, 3], 123),
            ([0, 1, None], 1),
            ([0, None, 1], 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6], 10478),
        ],
    )
    def test_sum_numbers(self, root_list: list[int | None], expected: int):
        result = run_sum_numbers(Solution, root_list)
        assert_sum_numbers(result, expected)
