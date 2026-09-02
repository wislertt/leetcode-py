import pytest

from leetcode_py import logged_test

from .helpers import assert_min_swaps, run_min_swaps
from .solution import Solution


class TestMinimumNumberOfSwapsToMakeTheStringBalanced:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("][][", 1),
            ("]]][[[", 2),
            ("[]", 0),
            ("][", 1),
            ("[[[]]]", 0),
            ("]][[", 1),
            ("[]][", 1),
            ("][][][", 1),
            ("]]]][[[[", 2),
            ("[]][[]", 1),
            ("]]][][[[", 2),
            ("]][[]][[", 1),
            ("[][]", 0),
            ("][[]", 1),
            ("[[]]][", 1),
            ("][][[]", 1),
            ("[[]][][]", 0),
            ("]][][[[]", 1),
            ("[[]]][[]", 1),
            ("[[[]]][[]]", 0),
            ("]][[][[]][", 1),
            ("]][][[]][[", 1),
            ("]]]][][[[[[]", 2),
            ("[]][[[[][]]]", 1),
            ("][[]][[[]]][", 1),
            ("]][]]][[[[][][[]", 2),
            ("]][]][][[]]][[[[", 2),
            ("]][[[]][][]][[][", 1),
        ],
    )
    def test_min_swaps(self, s: str, expected: int):
        result = run_min_swaps(Solution, s)
        assert_min_swaps(result, expected)
