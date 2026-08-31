import pytest

from leetcode_py import logged_test

from .helpers import assert_push_dominoes, run_push_dominoes
from .solution import Solution


class TestPushDominoes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "dominoes, expected",
        [
            ("RR.L", "RR.L"),
            (".L.R...LR..L..", "LL.RR.LLRRLL.."),
            (".", "."),
            ("L", "L"),
            ("R", "R"),
            ("L.", "L."),
            (".L", "LL"),
            ("R.", "RR"),
            (".R", ".R"),
            ("R...L", "RR.LL"),
            ("L...R", "L...R"),
            ("R.L", "R.L"),
            (".L.R.", "LL.RR"),
            ("R....L....R", "RRRLLL....R"),
            ("R.R.L", "RRR.L"),
            ("....L...R.....RRRLLL.....", "LLLLL...RRRRRRRRRLLL....."),
        ],
    )
    def test_push_dominoes(self, dominoes: str, expected: str):
        result = run_push_dominoes(Solution, dominoes)
        assert_push_dominoes(result, expected)
