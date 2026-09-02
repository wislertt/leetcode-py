import pytest

from leetcode_py import logged_test

from .helpers import assert_count_segments, run_count_segments
from .solution import Solution


class TestNumberSegmentsInAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("Hello, my name is John", 5),
            ("Hello", 1),
            ("", 0),
            (" ", 0),
            ("   ", 0),
            ("a", 1),
            (" a", 1),
            ("a ", 1),
            ("  a  ", 1),
            ("a  b", 2),
            ("  a  b  c  ", 3),
            ("Hello, my name is John and I love  programming", 9),
            ("!@#$%^&*()_+-=',.:", 1),
            ("x ! y", 3),
            ("0 1 2 3", 4),
            ("Run  run  run", 3),
            ("a b c d e f g h", 8),
            ("c*0$*:!aZ^'", 1),
            ("@Y#(b..b@cX=Z", 1),
            ("0*:", 1),
        ],
    )
    def test_count_segments(self, s: str, expected: int):
        result = run_count_segments(Solution, s)
        assert_count_segments(result, expected)
