import pytest

from leetcode_py import logged_test

from .helpers import assert_fair_candy_swap, run_fair_candy_swap
from .solution import Solution


class TestFairCandySwap:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "alice_sizes, bob_sizes, expected",
        [
            ([1, 1], [2, 2], [1, 2]),
            ([1, 2], [2, 3], [1, 2]),
            ([2], [1, 3], [2, 3]),
            ([1, 3], [2], [3, 2]),
            ([2, 4, 6, 8], [1, 3, 7, 11], [2, 3]),
            ([5, 5], [4, 4], [5, 4]),
            ([1, 2, 3], [4, 5, 7], [2, 7]),
            ([10, 20, 30], [5, 25, 40], [20, 25]),
            ([100], [25, 125], [100, 125]),
            ([99998, 1], [99997], [99998, 99997]),
            ([1, 1, 1, 1], [2, 4], [1, 2]),
            ([8, 12], [5, 13, 14], [8, 14]),
            ([4, 5, 6, 7, 8], [3, 25], [4, 3]),
            ([20], [5, 25], [20, 25]),
            ([70, 30, 50], [10, 100], [30, 10]),
            ([3, 3, 3, 9], [2, 14], [3, 2]),
            ([2, 2], [1, 2, 3], [2, 3]),
            ([7, 14, 21], [3, 17], [14, 3]),
        ],
    )
    def test_fair_candy_swap(
        self, alice_sizes: list[int], bob_sizes: list[int], expected: list[int]
    ):
        result = run_fair_candy_swap(Solution, alice_sizes, bob_sizes)
        assert_fair_candy_swap(result, expected)
