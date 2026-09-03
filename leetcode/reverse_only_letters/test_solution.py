import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_only_letters, run_reverse_only_letters
from .solution import Solution


class TestReverseOnlyLetters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ab-cd", "dc-ba"),
            ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
            ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
            ("a", "a"),
            ("z", "z"),
            ("-", "-"),
            ("ab", "ba"),
            ("A-b", "b-A"),
            ("!a!b!", "!b!a!"),
            ("12345", "12345"),
            ("a1b2c3", "c1b2a3"),
            ("QWERTY", "YTREWQ"),
            ("Ab,cD", "Dc,bA"),
            ("[]", "[]"),
            ("xyz!abc", "cba!zyx"),
            ("a!", "a!"),
            ("!a", "!a"),
            ("7-c", "7-c"),
            ("AbCdEf", "fEdCbA"),
            ("]a[b]c<", "]c[b]a<"),
            ("a0b1c2d3e4", "e0d1c2b3a4"),
            ("zZ-yY-xX", "Xx-Yy-Zz"),
        ],
    )
    def test_reverse_only_letters(self, s: str, expected: str):
        result = run_reverse_only_letters(Solution, s)
        assert_reverse_only_letters(result, expected)
