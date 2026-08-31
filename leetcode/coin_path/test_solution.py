import pytest

from leetcode_py import logged_test

from .helpers import assert_cheapest_jump, run_cheapest_jump
from .solution import Solution


class TestCoinPath:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "coins, max_jump, expected",
        [
            ([1, 2, 4, -1, 2], 2, [1, 3, 5]),
            ([1, 2, 4, -1, 2], 1, []),
            ([3], 1, [1]),
            ([-1], 1, []),
            ([0, 0, 0], 2, [1, 2, 3]),
            ([1, -1, 1], 1, []),
            ([5, -1, 5, -1, 5], 2, [1, 3, 5]),
            ([2, 1, 1, 2], 3, [1, 4]),
            ([1, 2, 3, 4, 5], 2, [1, 3, 5]),
            ([8, -1, 6, -1, 4, -1, 2], 2, [1, 3, 5, 7]),
            ([1, 1, 100, 1], 2, [1, 2, 4]),
            ([4, 12, 2, 4, 1, -1, 6], 3, [1, 3, 5, 7]),
            ([1, -1, -1, 1], 3, [1, 4]),
            ([7, 3, -1, 5, 2], 4, [1, 5]),
            ([1, 5, 3, 6, 2, -1, 4], 2, [1, 3, 5, 7]),
        ],
    )
    def test_cheapest_jump(self, coins: list[int], max_jump: int, expected: list[int]):
        result = run_cheapest_jump(Solution, coins, max_jump)
        assert_cheapest_jump(result, expected)
