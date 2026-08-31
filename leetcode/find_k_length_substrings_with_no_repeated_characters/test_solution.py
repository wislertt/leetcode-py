import pytest

from leetcode_py import logged_test

from .helpers import assert_num_k_len_substr_no_repeats, run_num_k_len_substr_no_repeats
from .solution import Solution


class TestFindKLengthSubstringsWithNoRepeatedCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("havefunonleetcode", 5, 6),
            ("home", 5, 0),
            ("abcabc", 3, 4),
            ("aaaa", 2, 0),
            ("a", 1, 1),
            ("abcdefg", 1, 7),
            ("abcdefg", 7, 1),
            ("abcdefg", 8, 0),
            ("abacaba", 3, 2),
            ("xyxyxy", 2, 5),
            ("zyxyxyz", 3, 2),
            ("abcba", 2, 4),
        ],
    )
    def test_num_k_len_substr_no_repeats(self, s: str, k: int, expected: int):
        result = run_num_k_len_substr_no_repeats(Solution, s, k)
        assert_num_k_len_substr_no_repeats(result, expected)
