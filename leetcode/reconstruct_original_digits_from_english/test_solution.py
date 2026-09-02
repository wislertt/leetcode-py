import pytest

from leetcode_py import logged_test

from .helpers import assert_original_digits, run_original_digits
from .solution import Solution


class TestReconstructOriginalDigitsFromEnglish:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("owoztneoer", "012"),
            ("fviefuro", "45"),
            ("zero", "0"),
            ("one", "1"),
            ("two", "2"),
            ("nine", "9"),
            ("zerozero", "00"),
            ("oneoneone", "111"),
            ("eight", "8"),
            ("sevenfive", "57"),
            ("rnzoenei", "09"),
            ("neoeoetwhtr", "123"),
            ("euxfsrfivoi", "456"),
            ("gnsnieeneviteh", "789"),
            ("uozwerterronheeofot", "01234"),
            ("enifessinnveeihvtgiex", "56789"),
            ("thetehertrhreee", "333"),
            ("ssiozixrxe", "066"),
            ("ffornoeronoueu", "1144"),
            ("iezrtreeeienvnirgsowtoounfvheiosextnefhe", "0123456789"),
            ("nweswsovvetetneo", "2277"),
            ("fvei", "5"),
        ],
    )
    def test_original_digits(self, s: str, expected: str):
        result = run_original_digits(Solution, s)
        assert_original_digits(result, expected)
