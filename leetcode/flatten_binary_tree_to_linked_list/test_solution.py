import pytest

from leetcode_py import logged_test

from .helpers import assert_flatten, run_flatten
from .solution import Solution


class TestFlattenBinaryTreeToLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
            ([], []),
            ([0], [0]),
            ([1, 2, 3], [1, None, 2, None, 3]),
            ([1, None, 2], [1, None, 2]),
            ([1, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]),
            ([1, None, 2, None, 3], [1, None, 2, None, 3]),
            ([3, 1, 2], [3, None, 1, None, 2]),
            ([-10, 9, 20, None, None, 15, 7], [-10, None, 9, None, 20, None, 15, None, 7]),
            ([1, 2, 5, 3, None, None, None, 4], [1, None, 2, None, 3, None, 4, None, 5]),
            ([44, -75], [44, None, -75]),
            ([60, 59], [60, None, 59]),
            ([35, 72, None, None, 32], [35, None, 72, None, 32]),
            ([53], [53]),
            ([35, -23, -6, None, None, None, 34], [35, None, -23, None, -6, None, 34]),
            ([47, 69], [47, None, 69]),
        ],
    )
    def test_flatten(self, root_list: list[int | None], expected: list[int | None]):
        result = run_flatten(Solution, root_list)
        assert_flatten(result, expected)
