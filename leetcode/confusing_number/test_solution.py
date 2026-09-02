import pytest

from leetcode_py import logged_test

from .helpers import assert_confusing_number, run_confusing_number
from .solution import Solution


class TestConfusingNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, False),
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, False),
            (6, True),
            (7, False),
            (8, False),
            (9, True),
            (10, True),
            (11, False),
            (12, False),
            (13, False),
            (14, False),
            (15, False),
            (16, True),
            (17, False),
            (18, True),
            (19, True),
            (20, False),
            (21, False),
            (22, False),
            (23, False),
            (24, False),
            (25, False),
            (26, False),
            (27, False),
            (28, False),
            (29, False),
            (30, False),
            (31, False),
            (32, False),
            (33, False),
            (34, False),
            (35, False),
            (36, False),
            (37, False),
            (38, False),
            (39, False),
            (69, False),
            (88, False),
            (96, False),
            (916, False),
            (619, False),
            (8000, True),
            (6109, True),
            (986, False),
            (1111, False),
            (25, False),
            (404, False),
            (6089, True),
            (9106, True),
            (689, False),
            (1069818, True),
            (999999999, True),
            (1000000000, True),
            (609, False),
            (11, False),
            (89, True),
            (6, True),
        ],
    )
    def test_confusing_number(self, n: int, expected: bool):
        result = run_confusing_number(Solution, n)
        assert_confusing_number(result, expected)
