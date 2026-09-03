import pytest

from leetcode_py import logged_test

from .helpers import assert_count_prime_set_bits, run_count_prime_set_bits
from .solution import Solution


class TestPrimeNumberOfSetBitsInBinaryRepresentation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "left, right, expected",
        [
            (6, 10, 4),
            (10, 15, 5),
            (1, 1, 0),
            (2, 2, 0),
            (3, 3, 1),
            (1, 2, 0),
            (1, 10, 6),
            (5, 8, 3),
            (9, 14, 6),
            (24, 28, 4),
            (32, 47, 11),
            (100, 130, 16),
            (567, 890, 164),
            (1, 1000, 530),
            (1000, 2000, 473),
            (12345, 13345, 380),
            (999990, 1000000, 5),
            (999999, 1000000, 1),
            (1, 5000, 2320),
            (524288, 525288, 474),
        ],
    )
    def test_count_prime_set_bits(self, left: int, right: int, expected: int):
        result = run_count_prime_set_bits(Solution, left, right)
        assert_count_prime_set_bits(result, expected)
