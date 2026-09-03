import pytest

from leetcode_py import logged_test

from .helpers import assert_find_integers, run_find_integers
from .solution import Solution


class TestNonNegativeIntegersWithoutConsecutiveOnes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 2),
            (2, 3),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 5),
            (7, 5),
            (8, 6),
            (9, 7),
            (10, 8),
            (11, 8),
            (16, 9),
            (21, 13),
            (32, 14),
            (63, 21),
            (64, 22),
            (100, 34),
            (127, 34),
            (128, 35),
            (255, 55),
            (256, 56),
            (511, 89),
            (512, 90),
            (1023, 144),
            (1024, 145),
            (4095, 377),
            (10000, 843),
            (65535, 2584),
            (123456, 4181),
            (1000000000, 2178309),
        ],
    )
    def test_find_integers(self, n: int, expected: int):
        result = run_find_integers(Solution, n)
        assert_find_integers(result, expected)
