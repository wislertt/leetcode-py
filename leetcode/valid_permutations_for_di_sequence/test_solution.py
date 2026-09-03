import pytest

from leetcode_py import logged_test

from .helpers import assert_num_perms_di_sequence, run_num_perms_di_sequence
from .solution import Solution


class TestValidPermutationsForDISequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("DID", 5),
            ("D", 1),
            ("I", 1),
            ("DD", 1),
            ("II", 1),
            ("DI", 2),
            ("ID", 2),
            ("IDI", 5),
            ("IID", 3),
            ("DDI", 3),
            ("IDID", 16),
            ("DIDIDID", 1385),
            ("IIIIIIII", 1),
            ("DDDDDDDD", 1),
            ("IIDDIIDDIIDDII", 120686411),
            ("IDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDID", 179476197),
            ("DIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDIDI", 179476197),
            ("IIIIIIIIIIIIIIIIIIIIDDDDDDDDDDDDDDDDDDDDIDIDIDIDIDIDIDIDIDID", 223405264),
            ("DDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDII", 622329892),
            ("IDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDIIDDI", 201935210),
        ],
    )
    def test_num_perms_di_sequence(self, s: str, expected: int):
        result = run_num_perms_di_sequence(Solution, s)
        assert_num_perms_di_sequence(result, expected)
