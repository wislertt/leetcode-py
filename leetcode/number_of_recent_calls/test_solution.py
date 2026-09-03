import pytest

from leetcode_py import logged_test

from .helpers import assert_recent_counter, run_recent_counter
from .solution import RecentCounter


class TestNumberOfRecentCalls:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["RecentCounter", "ping", "ping", "ping", "ping"],
                [[], [1], [100], [3001], [3002]],
                [None, 1, 2, 3, 3],
            ),
            (["RecentCounter", "ping"], [[], [1]], [None, 1]),
            (["RecentCounter", "ping", "ping"], [[], [1], [2]], [None, 1, 2]),
            (["RecentCounter", "ping", "ping"], [[], [1], [3001]], [None, 1, 2]),
            (["RecentCounter", "ping", "ping"], [[], [2], [3002]], [None, 1, 2]),
            (["RecentCounter", "ping", "ping", "ping"], [[], [1], [3002], [6003]], [None, 1, 1, 1]),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
                [[], [642], [1849], [4921], [5936], [5957]],
                [None, 1, 2, 1, 2, 3],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
                [[], [1], [100], [3001], [3002], [8000]],
                [None, 1, 2, 3, 3, 1],
            ),
            (["RecentCounter", "ping", "ping"], [[], [999999999], [1000000000]], [None, 1, 2]),
            (
                [
                    "RecentCounter",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                ],
                [[], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],
                [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            ),
            (
                [
                    "RecentCounter",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                ],
                [
                    [],
                    [1],
                    [2],
                    [3],
                    [4],
                    [5],
                    [6],
                    [7],
                    [8],
                    [9],
                    [10],
                    [11],
                    [12],
                    [13],
                    [14],
                    [15],
                ],
                [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
                [[], [1], [3000], [6000], [9000], [12000]],
                [None, 1, 2, 2, 2, 2],
            ),
            (
                [
                    "RecentCounter",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                ],
                [[], [1], [2], [3], [3000], [3001], [3002], [6000], [6001], [6002]],
                [None, 1, 2, 3, 4, 5, 5, 4, 4, 4],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping", "ping", "ping"],
                [[], [1], [4], [5], [3005], [3006], [6006], [9007]],
                [None, 1, 2, 3, 2, 2, 2, 1],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
                [[], [1501], [3001], [3002], [6002], [6003]],
                [None, 1, 2, 3, 2, 2],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping", "ping"],
                [[], [3], [8], [13], [14], [3014], [3015]],
                [None, 1, 2, 3, 4, 2, 2],
            ),
            (
                [
                    "RecentCounter",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                    "ping",
                ],
                [[], [2], [1502], [1503], [1505], [6505], [6605], [8105], [8205], [11205]],
                [None, 1, 2, 3, 4, 1, 2, 3, 4, 2],
            ),
            (
                ["RecentCounter", "ping", "ping", "ping", "ping", "ping"],
                [[], [3001], [6001], [6003], [6103], [6203]],
                [None, 1, 2, 2, 3, 4],
            ),
        ],
    )
    def test_recent_counter(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_recent_counter(RecentCounter, operations, inputs)
        assert_recent_counter(result, expected)
