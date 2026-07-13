import pytest

from leetcode_py import logged_test

from .helpers import assert_convert_to_title, run_convert_to_title
from .solution import Solution


class TestTestExcelSheetColumnTitle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, column_number, expected",
        [
            (Solution, 1, "A"),
            (Solution, 2, "B"),
            (Solution, 26, "Z"),
            (Solution, 27, "AA"),
            (Solution, 28, "AB"),
            (Solution, 52, "AZ"),
            (Solution, 53, "BA"),
            (Solution, 701, "ZY"),
            (Solution, 702, "ZZ"),
            (Solution, 703, "AAA"),
            (Solution, 18278, "ZZZ"),
            (Solution, 18279, "AAAA"),
            (Solution, 26, "Z"),
            (Solution, 78, "BZ"),
            (Solution, 79, "CA"),
            (Solution, 676, "YZ"),
            (Solution, 677, "ZA"),
            (Solution, 2147483647, "FXSHRXW"),
        ],
    )
    def test_convert_to_title(self, solution_class, column_number: int, expected: str):
        result = run_convert_to_title(solution_class, column_number)
        assert_convert_to_title(result, expected)
