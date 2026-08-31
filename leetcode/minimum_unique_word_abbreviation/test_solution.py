import pytest

from leetcode_py import logged_test

from .helpers import assert_min_abbreviation, run_min_abbreviation
from .solution import Solution


class TestMinimumUniqueWordAbbreviation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, dictionary",
        [
            ("apple", ["blade"]),
            ("apple", ["blade", "plain", "amber"]),
            ("a", []),
            ("abc", []),
            ("abc", ["xbc"]),
            ("abcd", ["abzz", "zzcd"]),
            ("aaaa", ["aaab", "baaa"]),
            ("target", []),
            ("leet", ["code"]),
            ("sword", []),
            ("abcd", []),
            ("goat", ["gate", "goal", "boat"]),
            ("world", ["would", "wound", "words"]),
            ("abcdefghij", ["abcdefghia", "zbcdefghij"]),
            ("ab", []),
            ("solve", ["salve", "solce", "solye"]),
        ],
    )
    def test_min_abbreviation(self, target: str, dictionary: list[str]):
        result = run_min_abbreviation(Solution, target, dictionary)
        assert_min_abbreviation(result, target, dictionary)
