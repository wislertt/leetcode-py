import pytest

from leetcode_py import logged_test

from .helpers import assert_find_the_longest_substring, run_find_the_longest_substring
from .solution import Solution


class TestFindTheLongestSubstringContainingVowelsInEvenCounts:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("eleetminicoworoep", 13),
            ("leetcodeisgreat", 5),
            ("bcbcbc", 6),
            ("a", 0),
            ("e", 0),
            ("b", 1),
            ("aa", 2),
            ("ae", 0),
            ("aeb", 1),
            ("aeiou", 0),
            ("aeioub", 1),
            ("aaaa", 4),
            ("abab", 4),
            ("aba", 3),
            ("aeiouaeiou", 10),
            ("aeioua", 0),
            ("bcdaeioubcd", 3),
            ("aaabbb", 5),
            ("aaaeee", 4),
            ("aeeeaaa", 4),
            ("iluqaohubfdlphmrdsha", 11),
            ("nifmfce", 4),
            ("toeeaaggffjkgrvugfgm", 13),
            ("alnfeickjt", 4),
            ("atvkcjljpkfppfbialm", 14),
            ("r", 1),
        ],
    )
    def test_find_the_longest_substring(self, s: str, expected: int):
        result = run_find_the_longest_substring(Solution, s)
        assert_find_the_longest_substring(result, expected)
