import pytest

from leetcode_py import logged_test

from .helpers import assert_least_ops_express_target, run_least_ops_express_target
from .solution import Solution


class TestLeastOperatorsToExpressNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, target, expected",
        [
            (3, 19, 5),
            (5, 501, 8),
            (100, 100000000, 3),
            (3, 365, 17),
            (2, 3, 2),
            (5, 5, 0),
            (2, 2, 0),
            (100, 1, 1),
            (2, 1, 1),
            (3, 1, 1),
            (10, 101, 3),
            (7, 100, 7),
            (2, 100000000, 107),
            (100, 199999999, 9),
            (2, 4, 1),
            (6, 3, 5),
            (5, 100, 4),
            (3, 729, 5),
            (2, 200000000, 113),
            (100, 99999999, 5),
        ],
    )
    def test_least_ops_express_target(self, x: int, target: int, expected: int):
        result = run_least_ops_express_target(Solution, x, target)
        assert_least_ops_express_target(result, expected)
