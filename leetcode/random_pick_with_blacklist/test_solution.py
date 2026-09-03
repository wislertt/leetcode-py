import pytest

from leetcode_py import logged_test

from .helpers import assert_pick, run_pick
from .solution import Solution


class TestRandomPickWithBlacklist:
    @logged_test
    @pytest.mark.parametrize(
        "n, blacklist, seed, calls",
        [
            (7, [2, 3, 5], 0, 1),
            (7, [2, 3, 5], 0, 500),
            (1, [], 0, 5),
            (2, [1], 0, 100),
            (2, [0], 3, 100),
            (3, [1], 0, 300),
            (4, [0, 1, 2], 5, 100),
            (5, [4], 0, 500),
            (6, [2, 4], 42, 500),
            (10, [], 0, 1000),
            (10, [0, 1, 2, 3, 4, 5, 6, 7, 8], 0, 200),
            (10, [0, 1, 2, 3, 4, 5, 6, 7], 1, 500),
            (20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 2000),
            (999999999, [0, 500000000], 0, 100),
            (1000000000, [], 5, 100),
            (1000000000, [1, 3, 999999999], 0, 100),
        ],
    )
    def test_pick(self, n: int, blacklist: list[int], seed: int, calls: int):
        result = run_pick(Solution, n, blacklist, seed, calls)
        assert_pick(result, n, blacklist, calls)
