import pytest

from leetcode_py import logged_test

from .helpers import assert_str2tree, run_str2tree
from .solution import Solution


class TestConstructBinaryTreeFromString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected_list",
        [
            ("4(2(3)(1))(6(5))", [4, 2, 6, 3, 1, 5]),
            ("4(2(3)(1))(6(5)(7))", [4, 2, 6, 3, 1, 5, 7]),
            ("-4(2(3)(1))(6(5)(7))", [-4, 2, 6, 3, 1, 5, 7]),
            ("", []),
            ("0", [0]),
            ("5", [5]),
            ("-1", [-1]),
            ("1073741824", [1073741824]),
            ("-1073741824", [-1073741824]),
            ("1(2)", [1, 2]),
            ("-8(3(9))", [-8, 3, None, 9]),
            ("2(1)(3)", [2, 1, 3]),
            ("7(4(2)(6))(10(9)(12))", [7, 4, 10, 2, 6, 9, 12]),
            ("3(1(0(7)))(5)", [3, 1, 5, 0, None, None, None, 7]),
            ("100(50(25(10)(30))(75(60)(80)))", [100, 50, None, 25, 75, 10, 30, 60, 80]),
            ("-15(-10(-20)(-5))(20(30))", [-15, -10, 20, -20, -5, 30]),
            ("-50(21(18(30)))", [-50, 21, None, 18, None, 30]),
            ("49(-21)(-30(-39)(-2))", [49, -21, -30, None, None, -39, -2]),
            ("29(-7)", [29, -7]),
            ("18(10(-49(-49)))(-26(33))", [18, 10, -26, -49, None, 33, None, -49]),
        ],
    )
    def test_str2tree(self, s: str, expected_list: list[int | None]):
        result = run_str2tree(Solution, s)
        assert_str2tree(result, expected_list)
