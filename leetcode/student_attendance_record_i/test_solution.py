import pytest

from leetcode_py import logged_test

from .helpers import assert_check_record, run_check_record
from .solution import Solution


class TestStudentAttendanceRecordI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("PPALLP", True),
            ("PPALLL", False),
            ("A", True),
            ("L", True),
            ("P", True),
            ("AA", False),
            ("LL", True),
            ("LLL", False),
            ("ALLAP", False),
            ("PAPPLP", True),
            ("LALL", True),
            ("PPALLPALL", False),
            ("LLLP", False),
            ("APPP", True),
            ("PPPPPP", True),
            ("ALLL", False),
            ("LLLALLL", False),
            ("AAALL", False),
            ("PPAAAALLL", False),
            ("AAPLPPLAL", False),
        ],
    )
    def test_check_record(self, s: str, expected: bool):
        result = run_check_record(Solution, s)
        assert_check_record(result, expected)
