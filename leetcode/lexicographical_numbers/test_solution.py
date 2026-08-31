import pytest

from leetcode_py import logged_test

from .helpers import assert_lexical_order, run_lexical_order
from .solution import Solution


class TestLexicographicalNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, [1]),
            (2, [1, 2]),
            (3, [1, 2, 3]),
            (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            (10, [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]),
            (11, [1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9]),
            (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
            (14, [1, 10, 11, 12, 13, 14, 2, 3, 4, 5, 6, 7, 8, 9]),
            (15, [1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9]),
            (19, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9]),
            (20, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]),
            (21, [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 3, 4, 5, 6, 7, 8, 9]),
        ],
    )
    def test_lexical_order(self, n: int, expected: list[int]):
        result = run_lexical_order(Solution, n)
        assert_lexical_order(result, expected)
