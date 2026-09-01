import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_pushes, run_minimum_pushes
from .solution import Solution


class TestMinimumNumberOfPushesToTypeWordII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("abcde", 5),
            ("xyzxyzxyzxyz", 12),
            ("aabbccddeeffgghhiiiiii", 24),
            ("a", 1),
            ("z", 1),
            ("aa", 2),
            ("ab", 2),
            ("abcdefgh", 8),
            ("abcdefghi", 10),
            ("abcdefghijklmnop", 24),
            ("abcdefghijklmnopqrstuvwxyz", 56),
            ("aaaaaaaaaaaaaaaaaaaa", 20),
            ("abababababababababab", 20),
            ("aaaaaaaaaaaaaaaaaaaaaaaa", 24),
            ("zzzyyyxxx", 9),
            ("qwertyuiopasdfghjklzxcvbnm", 56),
        ],
    )
    def test_minimum_pushes(self, word: str, expected: int):
        result = run_minimum_pushes(Solution, word)
        assert_minimum_pushes(result, expected)
