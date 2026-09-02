import pytest

from leetcode_py import logged_test

from .helpers import assert_title_to_number, run_title_to_number
from .solution import Solution


class TestTestExcelSheetColumnNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, column_title, expected",
        [
            (Solution, "A", 1),
            (Solution, "B", 2),
            (Solution, "Z", 26),
            (Solution, "AA", 27),
            (Solution, "AB", 28),
            (Solution, "AZ", 52),
            (Solution, "BA", 53),
            (Solution, "ZY", 701),
            (Solution, "ZZ", 702),
            (Solution, "AAA", 703),
            (Solution, "AZA", 1353),
            (Solution, "BZZ", 2054),
            (Solution, "ABC", 731),
            (Solution, "XYZ", 16900),
            (Solution, "ZZZZZ", 12356630),
            (Solution, "AAAAAAA", 321272407),
            (Solution, "FXSHRXW", 2147483647),
            (Solution, "DWZTVFZ", 1521182702),
            (Solution, "HVUR", 156044),
            (Solution, "YBJTEX", 298137786),
        ],
    )
    def test_title_to_number(self, solution_class, column_title: str, expected: int):
        result = run_title_to_number(solution_class, column_title)
        assert_title_to_number(result, expected)
