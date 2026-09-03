import pytest

from leetcode_py import logged_test

from .helpers import assert_prime_palindrome, run_prime_palindrome
from .solution import Solution


class TestPrimePalindrome:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 2),
            (2, 2),
            (3, 3),
            (4, 5),
            (5, 5),
            (6, 7),
            (8, 11),
            (9, 11),
            (10, 11),
            (11, 11),
            (12, 101),
            (13, 101),
            (14, 101),
            (31, 101),
            (98, 101),
            (99, 101),
            (100, 101),
            (101, 101),
            (102, 131),
            (130, 131),
            (132, 151),
            (200, 313),
            (1000, 10301),
            (10000, 10301),
            (123456, 1003001),
            (1000000, 1003001),
            (9999998, 100030001),
            (10000000, 100030001),
            (99999998, 100030001),
            (100000000, 100030001),
        ],
    )
    def test_prime_palindrome(self, n: int, expected: int):
        result = run_prime_palindrome(Solution, n)
        assert_prime_palindrome(result, expected)
