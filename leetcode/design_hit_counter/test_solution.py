import pytest

from leetcode_py import logged_test

from .helpers import assert_hit_counter, run_hit_counter
from .solution import HitCounter


class TestDesignHitCounter:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["HitCounter", "hit", "hit", "hit", "get_hits", "hit", "get_hits", "get_hits"],
                [[], [1], [2], [3], [4], [300], [300], [301]],
                [None, None, None, None, 3, None, 4, 3],
            ),
            (["HitCounter", "hit", "get_hits"], [[], [1], [1]], [None, None, 1]),
            (["HitCounter", "hit", "get_hits"], [[], [1], [301]], [None, None, 0]),
            (["HitCounter", "hit", "get_hits"], [[], [1], [300]], [None, None, 1]),
            (
                ["HitCounter", "hit", "hit", "hit", "get_hits"],
                [[], [5], [5], [5], [5]],
                [None, None, None, None, 3],
            ),
            (["HitCounter", "get_hits"], [[], [100]], [None, 0]),
            (
                ["HitCounter", "hit", "hit", "get_hits", "get_hits"],
                [[], [1], [300], [300], [301]],
                [None, None, None, 2, 1],
            ),
            (
                ["HitCounter", "hit", "get_hits", "hit", "get_hits"],
                [[], [1], [10], [10], [10]],
                [None, None, 1, None, 2],
            ),
            (
                ["HitCounter", "hit", "hit", "hit", "get_hits"],
                [[], [1], [2], [3], [3]],
                [None, None, None, None, 3],
            ),
            (
                ["HitCounter", "hit", "get_hits", "hit", "get_hits"],
                [[], [1], [301], [301], [301]],
                [None, None, 0, None, 1],
            ),
            (["HitCounter", "hit", "get_hits"], [[], [1], [302]], [None, None, 0]),
            (
                ["HitCounter", "hit", "hit", "get_hits"],
                [[], [299], [300], [300]],
                [None, None, None, 2],
            ),
            (
                ["HitCounter", "hit", "get_hits", "get_hits"],
                [[], [50], [349], [350]],
                [None, None, 1, 0],
            ),
        ],
    )
    def test_hit_counter(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_hit_counter(HitCounter, operations, inputs)
        assert_hit_counter(result, expected)
