import pytest

from leetcode_py import logged_test

from .helpers import assert_equations_possible, run_equations_possible
from .solution import Solution


class TestSatisfiabilityOfEqualityEquations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "equations, expected",
        [
            (["a==b", "b!=a"], False),
            (["b==a", "a==b"], True),
            (["a==b", "b==c", "a==c"], True),
            (["a==b", "b!=c", "c==a"], False),
            (["a!=a"], False),
            (["a==a"], True),
            (["a!=b"], True),
            (["a==b", "b==c", "c!=a"], False),
            (["c==c", "b==d", "x!=z"], True),
            (["a==b", "b==c", "c==d", "d!=a"], False),
            (["a!=b", "b!=c", "c!=a"], True),
            (["a==b", "e==e", "a!=e"], True),
            (["a==b", "b==a", "c==d", "d!=c"], False),
            (["f==a", "a==b", "b==f", "f!=a"], False),
            (["a==b", "b==c", "c==d", "e!=f", "f==e"], False),
            (["e==d", "e==a", "a!=d"], False),
            (["a==b", "b==c", "c==a", "a!=b"], False),
            (["g!=e", "c==c", "e==g"], False),
        ],
    )
    def test_equations_possible(self, equations: list[str], expected: bool):
        result = run_equations_possible(Solution, equations)
        assert_equations_possible(result, expected)
