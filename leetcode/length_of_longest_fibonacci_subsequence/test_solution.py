import pytest

from leetcode_py import logged_test

from .helpers import assert_len_longest_fib_subsequence, run_len_longest_fib_subsequence
from .solution import Solution


class TestLengthOfLongestFibonacciSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8], 5),
            ([1, 3, 7, 11, 12, 14, 18], 3),
            ([1, 2, 3], 3),
            ([1, 2, 4], 0),
            ([1, 2, 3, 5], 4),
            ([1, 2, 3, 5, 8], 5),
            ([1, 4, 5, 9], 4),
            ([2, 4, 6, 10, 16], 5),
            ([1, 3, 4, 7, 11], 5),
            ([10, 20, 30, 50, 80], 5),
            ([5, 6, 7, 8], 0),
            ([1, 100, 200, 300], 3),
            ([1, 2, 3, 4, 5, 6, 7, 8, 13, 21], 7),
            ([1, 2, 3, 4], 3),
        ],
    )
    def test_len_longest_fib_subsequence(self, arr: list[int], expected: int):
        result = run_len_longest_fib_subsequence(Solution, arr)
        assert_len_longest_fib_subsequence(result, expected)
