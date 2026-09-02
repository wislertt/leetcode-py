import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumNumberOfOperationsToMoveAllBallsToEachBox:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "boxes, expected",
        [
            ("110", [1, 1, 3]),
            ("001011", [11, 8, 5, 4, 3, 4]),
            ("0", [0]),
            ("1", [0]),
            ("10", [0, 1]),
            ("01", [1, 0]),
            ("11", [1, 1]),
            ("101", [2, 2, 2]),
            ("100", [0, 1, 2]),
            ("001", [2, 1, 0]),
            ("111", [3, 2, 3]),
            ("0101", [4, 2, 2, 2]),
            ("11010", [4, 3, 4, 5, 8]),
            ("000000", [0, 0, 0, 0, 0, 0]),
            ("101010101", [20, 17, 14, 13, 12, 13, 14, 17, 20]),
            ("11101", [7, 5, 5, 7, 9]),
            ("1100111", [16, 13, 12, 11, 10, 11, 14]),
            ("1010001", [8, 7, 6, 7, 8, 9, 10]),
            ("0110100110", [22, 17, 14, 13, 12, 13, 14, 15, 18, 23]),
        ],
    )
    def test_min_operations(self, boxes: str, expected: list[int]):
        result = run_min_operations(Solution, boxes)
        assert_min_operations(result, expected)
