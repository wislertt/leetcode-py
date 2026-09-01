import pytest

from leetcode_py import logged_test

from .helpers import assert_print_linked_list_in_reverse, run_print_linked_list_in_reverse
from .solution import Solution


class TestPrintImmutableLinkedListInReverse:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "values, expected",
        [
            ([1, 2, 3, 4], [4, 3, 2, 1]),
            ([0, -4, -1, 3, -5], [-5, 3, -1, -4, 0]),
            ([-2, 0, 6, 4, 4, -6], [-6, 4, 4, 6, 0, -2]),
            ([7], [7]),
            ([5, 9], [9, 5]),
            ([1, 1, 1], [1, 1, 1]),
            ([1000, -1000], [-1000, 1000]),
            ([3, 7, 3, 7, 3], [3, 7, 3, 7, 3]),
            ([0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0]),
            ([10, 20, 30, 40, 50, 60], [60, 50, 40, 30, 20, 10]),
            ([9, 8, 7], [7, 8, 9]),
            ([-1, -2, -3, -4, -5, -6, -7, -8], [-8, -7, -6, -5, -4, -3, -2, -1]),
            ([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]),
            ([-771], [-771]),
        ],
    )
    def test_print_linked_list_in_reverse(self, values: list[int], expected: list[int]):
        result = run_print_linked_list_in_reverse(Solution, values)
        assert_print_linked_list_in_reverse(result, expected)
