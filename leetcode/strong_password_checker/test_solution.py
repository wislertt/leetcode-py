import pytest

from leetcode_py import logged_test

from .helpers import assert_strong_password_checker, run_strong_password_checker
from .solution import Solution


class TestStrongPasswordChecker:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "password, expected",
        [
            ("a", 5),
            ("aA1", 3),
            ("1337C0d3", 0),
            ("aaa", 3),
            ("aaaa", 2),
            ("aaaaa", 2),
            ("aaaaaa", 2),
            ("111111", 2),
            ("aA1aaa", 1),
            (".aA1!", 1),
            ("aaaaa1", 1),
            ("aaaaaaaaaa", 3),
            ("aaaaaaaaaaaaaaaaaaaa", 6),
            ("aaaaaaaaaaaaaaaaaaaaa", 7),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 36),
            ("abcabcabcabcabcabcabcabcabcabc", 12),
            ("aaaaabbbbbcccccdddddeeeeefffff", 13),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 16),
            ("aa!", 3),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaa1A", 14),
            ("!!!!!aaaaa", 2),
            ("aaa.bbb.ccc.ddd", 4),
            ("aaaaaaaaaaaa", 4),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 16),
        ],
    )
    def test_strong_password_checker(self, password: str, expected: int):
        result = run_strong_password_checker(Solution, password)
        assert_strong_password_checker(result, expected)
