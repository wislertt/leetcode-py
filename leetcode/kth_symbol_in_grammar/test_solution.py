import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_grammar, run_kth_grammar
from .solution import Solution


class TestKthSymbolInGrammar:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (1, 1, 0),
            (2, 1, 0),
            (2, 2, 1),
            (3, 1, 0),
            (3, 2, 1),
            (3, 3, 1),
            (3, 4, 0),
            (4, 5, 1),
            (4, 8, 1),
            (5, 11, 0),
            (30, 1, 0),
            (30, 2, 1),
            (30, 434991989, 0),
            (30, 536870912, 1),
        ],
    )
    def test_kth_grammar(self, n: int, k: int, expected: int):
        result = run_kth_grammar(Solution, n, k)
        assert_kth_grammar(result, expected)
