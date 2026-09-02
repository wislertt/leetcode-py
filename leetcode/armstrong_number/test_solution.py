import pytest

from leetcode_py import logged_test

from .helpers import assert_is_armstrong, run_is_armstrong
from .solution import Solution


class TestArmstrongNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, True),
            (2, True),
            (9, True),
            (10, False),
            (99, False),
            (100, False),
            (153, True),
            (370, True),
            (371, True),
            (407, True),
            (1634, True),
            (8208, True),
            (9474, True),
            (54748, True),
            (92727, True),
            (93084, True),
            (548834, True),
            (1741725, True),
            (4210818, True),
            (9800817, True),
            (9926315, True),
            (24678050, True),
            (24678051, True),
            (88593477, True),
            (100000000, False),
            (99999999, False),
            (123, False),
            (152, False),
            (154, False),
            (12, False),
            (8209, False),
            (12345, False),
        ],
    )
    def test_is_armstrong(self, n: int, expected: bool):
        result = run_is_armstrong(Solution, n)
        assert_is_armstrong(result, expected)
