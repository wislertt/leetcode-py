import pytest

from leetcode_py import logged_test

from .helpers import assert_mask_pii, run_mask_pii
from .solution import Solution


class TestMaskingPersonalInformation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("LeetCode@LeetCode.com", "l*****e@leetcode.com"),
            ("AB@qq.com", "a*****b@qq.com"),
            ("aBcD@xYz.com", "a*****d@xyz.com"),
            ("abc@code.org", "a*****c@code.org"),
            ("Worker@LeetCode.com", "w*****r@leetcode.com"),
            ("xy@mailserver.com", "x*****y@mailserver.com"),
            ("ruh@ftqv.kc", "r*****h@ftqv.kc"),
            ("LwWcQjGQ@nsscuxk.xz", "l*****q@nsscuxk.xz"),
            ("wXAWrww@jyvd.lyp", "w*****w@jyvd.lyp"),
            ("1(234)567-890", "***-***-7890"),
            ("123-456-7890", "***-***-7890"),
            ("(123) 456-7890", "***-***-7890"),
            ("1234567890", "***-***-7890"),
            ("+1 234 567 8901", "+*-***-***-8901"),
            ("861234567890", "+**-***-***-7890"),
            ("+999-999-999-999", "+**-***-***-9999"),
            ("1(111)111-1111", "+*-***-***-1111"),
            ("+111 111 111 1111", "+***-***-***-1111"),
            ("1 234 567 8901", "+*-***-***-8901"),
            ("2 7(431 54+622", "***-***-4622"),
            ("36 1 652)24-9 79", "+*-***-***-4979"),
            ("6(64+4)9+42-96 951", "+**-***-***-6951"),
            ("15+40424+0+4 2939", "+***-***-***-2939"),
        ],
    )
    def test_mask_pii(self, s: str, expected: str):
        result = run_mask_pii(Solution, s)
        assert_mask_pii(result, expected)
