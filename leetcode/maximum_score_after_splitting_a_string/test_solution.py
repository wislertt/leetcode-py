import pytest

from leetcode_py import logged_test

from .helpers import assert_max_score, run_max_score
from .solution import Solution


class TestMaximumScoreAfterSplittingAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("011101", 5),
            ("00111", 5),
            ("1111", 3),
            ("0000", 3),
            ("00", 1),
            ("11", 1),
            ("01", 2),
            ("10", 0),
            ("0101", 3),
            ("1010", 2),
            ("000111", 6),
            ("111000", 2),
            ("11100", 2),
            ("01010111", 6),
            ("1100", 1),
            ("01110110", 6),
            ("000111100", 7),
            ("0010100100", 6),
            ("1110", 2),
            ("01100000", 5),
        ],
    )
    def test_max_score(self, s: str, expected: int):
        result = run_max_score(Solution, s)
        assert_max_score(result, expected)
