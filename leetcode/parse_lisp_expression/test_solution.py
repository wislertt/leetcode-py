import pytest

from leetcode_py import logged_test

from .helpers import assert_evaluate, run_evaluate
from .solution import Solution


class TestParseLispExpression:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("(let x 2 (mult x (let x 3 y 4 (add x y))))", 14),
            ("(let x 3 x 2 x)", 2),
            ("(let x 1 y 2 x (add x y) (add x y))", 5),
            ("(add 1 2)", 3),
            ("(mult 3 4)", 12),
            ("(add (add 1 2) (mult 3 4))", 15),
            ("7", 7),
            ("-3", -3),
            ("(let x 7 x)", 7),
            ("(let x -2 y x y)", -2),
            ("(let a1 3 b2 (add a1 1) b2)", 4),
            ("(let x 2 (add (let x 3 x) x))", 5),
            ("(mult -3 (add 2 2))", -12),
            ("(let x 1 (add x (let x 2 x)))", 3),
            ("(let v 5 (mult v (let v 2 (add v 1))))", 15),
            ("(add (let x 2 x) (let y 3 y))", 5),
            ("(let x 2 (mult x 5))", 10),
            ("(let x 0 (add x (mult x 9)))", 0),
        ],
    )
    def test_evaluate(self, expression: str, expected: int):
        result = run_evaluate(Solution, expression)
        assert_evaluate(result, expected)
