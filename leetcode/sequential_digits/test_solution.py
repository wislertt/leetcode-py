import pytest

from leetcode_py import logged_test

from .helpers import assert_sequential_digits, run_sequential_digits
from .solution import Solution


class TestSequentialDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "low, high, expected",
        [
            (100, 300, [123, 234]),
            (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
            (
                10,
                1000000000,
                [
                    12,
                    23,
                    34,
                    45,
                    56,
                    67,
                    78,
                    89,
                    123,
                    234,
                    345,
                    456,
                    567,
                    678,
                    789,
                    1234,
                    2345,
                    3456,
                    4567,
                    5678,
                    6789,
                    12345,
                    23456,
                    34567,
                    45678,
                    56789,
                    123456,
                    234567,
                    345678,
                    456789,
                    1234567,
                    2345678,
                    3456789,
                    12345678,
                    23456789,
                    123456789,
                ],
            ),
            (58, 66, []),
            (123, 123, [123]),
            (10, 23, [12, 23]),
            (6789, 6790, [6789]),
            (123456789, 999999999, [123456789]),
            (100, 122, []),
            (10000, 99999, [12345, 23456, 34567, 45678, 56789]),
            (124, 122, []),
            (90, 125, [123]),
        ],
    )
    def test_sequential_digits(self, low: int, high: int, expected: list[int]):
        result = run_sequential_digits(Solution, low, high)
        assert_sequential_digits(result, expected)
