import pytest

from leetcode_py import logged_test

from .helpers import assert_self_dividing_numbers, run_self_dividing_numbers
from .solution import Solution


class TestSelfDividingNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "left, right, expected",
        [
            (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
            (47, 85, [48, 55, 66, 77]),
            (1, 1, [1]),
            (1, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            (1, 13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]),
            (10, 12, [11, 12]),
            (13, 15, [15]),
            (20, 25, [22, 24]),
            (26, 33, [33]),
            (38, 40, []),
            (48, 48, [48]),
            (55, 66, [55, 66]),
            (88, 88, [88]),
            (99, 111, [99, 111]),
            (100, 120, [111, 112, 115]),
            (128, 128, [128]),
            (2222, 2222, [2222]),
            (9990, 9999, [9999]),
            (9999, 9999, [9999]),
            (1000, 1010, []),
            (9000, 9000, []),
            (11, 11, [11]),
            (111, 111, [111]),
            (2022, 2022, []),
        ],
    )
    def test_self_dividing_numbers(self, left: int, right: int, expected: list[int]):
        result = run_self_dividing_numbers(Solution, left, right)
        assert_self_dividing_numbers(result, expected)
