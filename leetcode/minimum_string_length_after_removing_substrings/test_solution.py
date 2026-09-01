import pytest

from leetcode_py import logged_test

from .helpers import assert_min_length, run_min_length
from .solution import Solution


class TestMinimumStringLengthAfterRemovingSubstrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ABFCACDB", 2),
            ("ACBBD", 5),
            ("A", 1),
            ("B", 1),
            ("C", 1),
            ("D", 1),
            ("AB", 0),
            ("CD", 0),
            ("ACDB", 0),
            ("ACBD", 4),
            ("AAAA", 4),
            ("ABABABAB", 0),
            ("CACDDB", 4),
            ("BACDAB", 2),
            ("ABCDAABB", 0),
            ("AABBCCDD", 0),
        ],
    )
    def test_min_length(self, s: str, expected: int):
        result = run_min_length(Solution, s)
        assert_min_length(result, expected)
