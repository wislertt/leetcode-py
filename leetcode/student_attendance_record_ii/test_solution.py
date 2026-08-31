import pytest

from leetcode_py import logged_test

from .helpers import assert_check_record, run_check_record
from .solution import Solution


class TestStudentAttendanceRecordII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 3),
            (2, 8),
            (3, 19),
            (4, 43),
            (5, 94),
            (6, 200),
            (7, 418),
            (8, 861),
            (9, 1753),
            (10, 3536),
            (11, 7077),
            (12, 14071),
            (13, 27820),
            (14, 54736),
            (10101, 183236316),
            (100000, 749184020),
        ],
    )
    def test_check_record(self, n: int, expected: int):
        result = run_check_record(Solution, n)
        assert_check_record(result, expected)
