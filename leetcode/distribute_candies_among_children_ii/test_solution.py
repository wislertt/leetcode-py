import pytest

from leetcode_py import logged_test

from .helpers import assert_distribute_candies, run_distribute_candies
from .solution import Solution


class TestDistributeCandiesAmongChildrenII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, limit, expected",
        [
            (5, 2, 3),
            (3, 3, 10),
            (1, 1, 3),
            (2, 1, 3),
            (3, 1, 1),
            (4, 1, 0),
            (6, 2, 1),
            (2, 5, 6),
            (7, 3, 6),
            (10, 4, 6),
            (18, 6, 1),
            (100, 50, 1326),
            (1000, 100, 0),
            (999999, 1, 0),
            (1000000, 1000000, 500001500001),
            (1000000, 333333, 0),
            (1000000, 500000, 125000750001),
            (999999, 333333, 1),
        ],
    )
    def test_distribute_candies(self, n: int, limit: int, expected: int):
        result = run_distribute_candies(Solution, n, limit)
        assert_distribute_candies(result, expected)
