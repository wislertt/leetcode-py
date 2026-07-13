import pytest

from leetcode_py import logged_test

from .helpers import assert_calc_equation, run_calc_equation
from .solution import Solution


class TestEvaluateDivision:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "equations, values, queries, expected",
        [
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
                [6.0, 0.5, -1.0, 1.0, -1.0],
            ),
            (
                [["a", "b"], ["b", "c"], ["bc", "cd"]],
                [1.5, 2.5, 5.0],
                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
                [3.75, 0.4, 5.0, 0.2],
            ),
            (
                [["a", "b"]],
                [0.5],
                [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
                [0.5, 2.0, -1.0, -1.0],
            ),
            ([["a", "b"]], [2.0], [["a", "b"]], [2.0]),
            ([["a", "b"]], [2.0], [["b", "a"]], [0.5]),
            ([["a", "b"]], [2.0], [["a", "a"]], [1.0]),
            ([["a", "b"]], [2.0], [["x", "y"]], [-1.0]),
            (
                [["a", "b"], ["b", "c"], ["c", "d"]],
                [2.0, 3.0, 4.0],
                [["a", "d"], ["d", "a"]],
                [24.0, 0.041666666666666664],
            ),
            ([["a", "b"], ["c", "d"]], [2.0, 3.0], [["a", "d"]], [-1.0]),
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["c", "a"], ["b", "b"], ["y", "z"]],
                [6.0, 0.16666666666666666, 1.0, -1.0],
            ),
            ([["a", "b"]], [1.0], [["a", "b"], ["b", "a"], ["a", "a"]], [1.0, 1.0, 1.0]),
            (
                [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]],
                [2.0, 2.0, 2.0, 2.0],
                [["a", "e"], ["e", "a"]],
                [16.0, 0.0625],
            ),
            (
                [["x1", "x2"], ["x2", "x3"]],
                [3.0, 4.0],
                [["x1", "x3"], ["x3", "x1"]],
                [12.0, 0.08333333333333333],
            ),
            ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["x", "x"]], [-1.0]),
            ([["a", "b"]], [5.0], [["a", "b"], ["b", "a"]], [5.0, 0.2]),
        ],
    )
    def test_calc_equation(
        self,
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]],
        expected: list[float],
    ):
        result = run_calc_equation(Solution, equations, values, queries)
        assert_calc_equation(result, expected)
