import pytest

from leetcode_py import logged_test

from .helpers import assert_get_length_of_optimal_compression, run_get_length_of_optimal_compression
from .solution import Solution


class TestStringCompressionII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("aaabcccd", 2, 4),
            ("aabbaa", 2, 2),
            ("aaaaaaaaaaa", 0, 3),
            ("a", 0, 1),
            ("a", 1, 0),
            ("abc", 0, 3),
            ("abc", 3, 0),
            ("aaabbaaa", 1, 5),
            ("abbccccc", 3, 2),
            ("aabbcc", 2, 4),
            ("aaaaaaaaaa", 1, 2),
            ("abababab", 4, 2),
            ("aaaabbbbc", 3, 4),
            ("aaaaaaaaaaaa", 5, 2),
            ("bacccacbacac", 5, 3),
            ("badddbdac", 3, 4),
            ("dddaacaddabb", 0, 11),
            ("daaacc", 3, 2),
            (
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                0,
                4,
            ),
            (
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                1,
                3,
            ),
            (
                "abababababababababababababababababababababababababababababababababababababababababababababababababab",
                100,
                0,
            ),
            (
                "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd",
                40,
                49,
            ),
        ],
    )
    def test_get_length_of_optimal_compression(self, s: str, k: int, expected: int):
        result = run_get_length_of_optimal_compression(Solution, s, k)
        assert_get_length_of_optimal_compression(result, expected)
