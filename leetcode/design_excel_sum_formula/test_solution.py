import pytest

from leetcode_py import logged_test

from .helpers import assert_excel_sum_formula, run_excel_sum_formula
from .solution import Excel


class TestDesignExcelSumFormula:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["Excel", "set", "sum", "set", "get"],
                [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]],
                [None, None, 4, None, 6],
            ),
            (
                ["Excel", "set", "sum", "get", "set", "get"],
                [[3, "C"], [1, "A", 2], [2, "B", ["A1"]], [2, "B"], [1, "A", 5], [2, "B"]],
                [None, None, 2, 2, None, 5],
            ),
            (
                ["Excel", "set", "sum", "set", "get"],
                [[2, "B"], [1, "A", 1], [2, "B", ["A1:A2"]], [2, "A", 3], [2, "B"]],
                [None, None, 1, None, 4],
            ),
            (
                ["Excel", "set", "sum", "sum", "get"],
                [[3, "C"], [1, "B", 7], [1, "A", ["B1"]], [2, "A", ["A1", "B1"]], [2, "A"]],
                [None, None, 7, 14, 14],
            ),
            (
                ["Excel", "set", "set", "set", "set", "sum", "get"],
                [
                    [5, "E"],
                    [1, "A", 1],
                    [1, "B", 2],
                    [2, "A", 3],
                    [2, "B", 4],
                    [3, "C", ["A1:B2"]],
                    [3, "C"],
                ],
                [None, None, None, None, None, 10, 10],
            ),
            (
                ["Excel", "set", "set", "sum", "get"],
                [[2, "A"], [1, "A", -5], [2, "A", 8], [2, "A", ["A1"]], [2, "A"]],
                [None, None, None, -5, -5],
            ),
            (
                ["Excel", "sum", "sum", "get", "get"],
                [[4, "D"], [1, "A", ["C1:C2"]], [4, "D", ["A1", "B1"]], [4, "D"], [1, "A"]],
                [None, 0, 0, 0, 0],
            ),
            (["Excel", "set", "get"], [[1, "A"], [1, "A", 42], [1, "A"]], [None, None, 42]),
            (["Excel", "get"], [[2, "B"], [1, "A"]], [None, 0]),
            (
                ["Excel", "sum", "set", "get", "get"],
                [[3, "C"], [3, "C", ["A1:A3"]], [3, "A", 10], [3, "C"], [3, "A"]],
                [None, 0, None, 10, 10],
            ),
            (
                ["Excel", "set", "sum", "get"],
                [[2, "B"], [1, "A", 6], [2, "B", ["A1", "A1"]], [2, "B"]],
                [None, None, 12, 12],
            ),
            (
                ["Excel", "set", "set", "sum", "get"],
                [[2, "C"], [1, "A", 1], [2, "C", 5], [1, "B", ["A1", "C2"]], [1, "B"]],
                [None, None, None, 6, 6],
            ),
        ],
    )
    def test_excel_sum_formula(
        self, operations: list[str], inputs: list[list], expected: list[int | None]
    ):
        result, _ = run_excel_sum_formula(Excel, operations, inputs)
        assert_excel_sum_formula(result, expected)
