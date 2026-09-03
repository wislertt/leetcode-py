import pytest

from leetcode_py import logged_test

from .helpers import assert_unique_letter_string, run_unique_letter_string
from .solution import Solution


class TestUniqueLetterString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ABC", 10),
            ("ABA", 8),
            ("LEETCODE", 92),
            ("A", 1),
            ("AA", 2),
            ("AB", 4),
            ("AAA", 3),
            ("AAB", 6),
            ("ABB", 6),
            ("ABAB", 12),
            ("AABC", 14),
            ("ABCA", 18),
            ("ABCDEFG", 84),
            ("AABBCC", 18),
            ("AABAA", 15),
            ("ZZZZZ", 5),
            ("AAACC", 10),
            ("OKKKIB", 28),
            ("ABBA", 10),
            ("FCDDNCF", 50),
            ("D", 1),
            ("OMDJEG", 56),
            ("IIGO", 14),
            ("ABDBCDCC", 53),
        ],
    )
    def test_unique_letter_string(self, s: str, expected: int):
        result = run_unique_letter_string(Solution, s)
        assert_unique_letter_string(result, expected)
