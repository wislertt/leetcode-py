import pytest

from leetcode_py import logged_test

from .helpers import assert_num_decodings, run_num_decodings
from .solution import Solution


class TestDecodeWaysII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("*", 9),
            ("1*", 18),
            ("2*", 15),
            ("0", 0),
            ("10", 1),
            ("01", 0),
            ("1", 1),
            ("12", 2),
            ("27", 1),
            ("**", 96),
            ("*1", 11),
            ("3*", 9),
            ("*0", 2),
            ("10*", 9),
            ("**0", 18),
            ("11106", 2),
            ("*1*", 180),
            ("90", 0),
            ("2*7", 16),
            ("**12", 210),
            ("1**", 177),
            ("0*", 0),
            ("6**25085", 0),
            ("36283", 1),
            ("2336", 2),
            ("845027", 0),
            ("4*87", 10),
            ("14934", 2),
            ("53340", 0),
            ("8065", 0),
        ],
    )
    def test_num_decodings(self, s: str, expected: int):
        result = run_num_decodings(Solution, s)
        assert_num_decodings(result, expected)
