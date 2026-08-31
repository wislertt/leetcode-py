import pytest

from leetcode_py import logged_test

from .helpers import assert_distribute_coins, run_distribute_coins
from .solution import Solution


class TestDistributeCoins:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 0, 0], 2),
            ([0, 3, 0], 3),
            ([1, 0, 0, None, 3], 4),
            ([1], 0),
            ([0, 0, 3], 3),
            ([4, 0, None, 0, None, 0], 6),
            ([1, 0, 2], 2),
            ([0, 0, None, 0, None, 4], 6),
            ([7, 0, 0, 0, 0, 0, 0], 10),
            ([2, 0, 0, 0, None, None, 3], 6),
            ([1, 2, 0], 2),
            ([0, 1, 0, None, 3], 5),
            ([2, 0, 0, None, 0, None, 3], 6),
            ([0, 0, 2, None, 2], 2),
        ],
    )
    def test_distribute_coins(self, root_list: list[int | None], expected: int):
        result = run_distribute_coins(Solution, root_list)
        assert_distribute_coins(result, expected)
