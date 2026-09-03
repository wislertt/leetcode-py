import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_smallest_prime_fraction, run_kth_smallest_prime_fraction
from .solution import Solution


class TestKThSmallestPrimeFraction:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, expected",
        [
            ([1, 2, 3, 5], 3, [2, 5]),
            ([1, 7], 1, [1, 7]),
            ([1, 2], 1, [1, 2]),
            ([1, 2, 3, 5], 1, [1, 5]),
            ([1, 2, 3, 5], 6, [2, 3]),
            ([1, 2, 3], 2, [1, 2]),
            ([1, 2, 3], 1, [1, 3]),
            ([1, 2, 3, 5, 7], 1, [1, 7]),
            ([1, 2, 3, 5, 7], 10, [5, 7]),
            ([1, 3, 5, 7, 11], 4, [3, 11]),
            ([1, 5, 13, 17], 3, [1, 5]),
            ([1, 2, 5, 11, 13, 17], 8, [5, 17]),
            ([1, 2, 3, 5, 7, 11, 13], 15, [1, 2]),
            ([1, 2, 3, 5, 7, 11, 13, 17], 20, [1, 2]),
            ([1, 7, 11], 3, [7, 11]),
            ([1, 11, 13, 17, 19], 7, [13, 19]),
            ([1, 7, 31, 43, 61, 89, 163, 181], 24, [89, 163]),
            ([1, 13, 17, 19, 31, 73, 151], 5, [1, 17]),
            ([1, 3, 23, 71, 149, 193], 14, [71, 149]),
            ([1, 89, 101, 149], 2, [1, 101]),
            ([1, 2, 127], 3, [1, 2]),
            ([1, 47, 127], 2, [1, 47]),
        ],
    )
    def test_kth_smallest_prime_fraction(self, arr: list[int], k: int, expected: list[int]):
        result = run_kth_smallest_prime_fraction(Solution, arr, k)
        assert_kth_smallest_prime_fraction(result, expected)
