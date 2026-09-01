import pytest

from leetcode_py import logged_test

from .helpers import assert_put_marbles, run_put_marbles
from .solution import Solution


class TestPutMarblesInBags:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "weights, k, expected",
        [
            ([1, 3, 5, 1], 2, 4),
            ([1, 3], 2, 0),
            ([1], 1, 0),
            ([5], 1, 0),
            ([1, 2, 3, 4, 5], 2, 6),
            ([1, 2, 3, 4, 5], 5, 0),
            ([4, 4, 4, 4], 3, 0),
            ([9, 1, 8, 2, 7, 3], 3, 2),
            ([1000000000, 1, 1000000000], 2, 0),
            ([1000000000, 1, 1, 1000000000], 2, 999999999),
            ([2, 7, 7, 5, 4, 2, 9, 1], 3, 11),
            ([3, 2, 1], 2, 2),
            ([6, 6, 6, 6, 6], 4, 0),
            ([10, 1, 1, 1, 10], 2, 9),
            ([7, 3, 9, 4, 2, 8, 1, 6], 4, 13),
            ([1, 2], 1, 0),
            ([1, 9, 1, 9, 1], 3, 0),
            ([1, 1, 1, 1, 1, 2], 2, 1),
        ],
    )
    def test_put_marbles(self, weights: list[int], k: int, expected: int):
        result = run_put_marbles(Solution, weights, k)
        assert_put_marbles(result, expected)
