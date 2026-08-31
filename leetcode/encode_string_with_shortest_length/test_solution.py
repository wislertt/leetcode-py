import pytest

from leetcode_py import logged_test

from .helpers import assert_encode, run_encode
from .solution import Solution


class TestEncodeStringWithShortestLength:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected_len",
        [
            ("aaa", 3),
            ("aaaaa", 4),
            ("aaaaaaaaaa", 5),
            ("abcabcabcabc", 6),
            ("abbbabbbcabbbabbbc", 11),
            ("a", 1),
            ("aa", 2),
            ("aaaa", 4),
            ("abababab", 5),
            ("aabcaabxaabc", 12),
            ("abcabcabcdabcde", 12),
            ("abababababababababababababababab", 6),
        ],
    )
    def test_encode(self, s: str, expected_len: int):
        result = run_encode(Solution, s)
        assert_encode(result, s, expected_len)
