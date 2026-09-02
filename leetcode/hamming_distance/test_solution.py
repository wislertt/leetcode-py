import pytest

from leetcode_py import logged_test

from .helpers import assert_hamming_distance, run_hamming_distance
from .solution import Solution


class TestHammingDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (1, 4, 2),
            (3, 1, 1),
            (0, 0, 0),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 0),
            (2, 1, 2),
            (7, 7, 0),
            (15, 0, 4),
            (0, 2147483647, 31),
            (2147483647, 2147483647, 0),
            (2147483647, 0, 31),
            (123456789, 987654321, 15),
            (1344025257, 286130530, 13),
            (1800652142, 743377863, 16),
            (379944512, 1813096935, 20),
            (1151405634, 2132125920, 16),
            (966455881, 825552887, 16),
            (1322570837, 2041244841, 20),
            (1528332448, 638467953, 20),
        ],
    )
    def test_hamming_distance(self, x: int, y: int, expected: int):
        result = run_hamming_distance(Solution, x, y)
        assert_hamming_distance(result, expected)
