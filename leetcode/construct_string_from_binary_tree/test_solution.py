import pytest

from leetcode_py import logged_test

from .helpers import assert_tree2str, run_tree2str
from .solution import Solution


class TestConstructStringFromBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4], "1(2(4))(3)"),
            ([1, 2, 3, None, 4], "1(2()(4))(3)"),
            ([1], "1"),
            ([1, 2], "1(2)"),
            ([1, None, 2], "1()(2)"),
            ([1, 2, 3], "1(2)(3)"),
            ([1, 2, None, 3], "1(2(3))"),
            ([-1, -2, -3, None, -4], "-1(-2()(-4))(-3)"),
            ([1, 2, 3, 4, 5, 6, 7], "1(2(4)(5))(3(6)(7))"),
            ([1, 2, None, None, 3], "1(2()(3))"),
            ([0, 0, 0], "0(0)(0)"),
            ([1, 2, 3, None, None, 4], "1(2)(3(4))"),
            ([5, None, 6, None, 7, None, 8], "5()(6()(7()(8)))"),
            ([1, None, 2, None, 3], "1()(2()(3))"),
        ],
    )
    def test_tree2str(self, root_list: list[int | None], expected: str):
        result = run_tree2str(Solution, root_list)
        assert_tree2str(result, expected)
