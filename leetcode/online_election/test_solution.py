import pytest

from leetcode_py import logged_test

from .helpers import assert_online_election, run_online_election
from .solution import TopVotedCandidate


class TestOnlineElection:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25]],
                [None, 0, 1, 1],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [15], [24], [8]],
                [None, 0, 0, 1],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [30], [29], [0]],
                [None, 0, 1, 0],
            ),
            (["TopVotedCandidate", "q", "q"], [[[0], [0]], [0], [1000000000]], [None, 0, 0]),
            (
                ["TopVotedCandidate", "q", "q", "q", "q"],
                [[[2, 2, 2], [1, 2, 3]], [1], [2], [3], [4]],
                [None, 2, 2, 2, 2],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q", "q"],
                [[[0, 1], [0, 10]], [0], [5], [10], [15]],
                [None, 0, 0, 1, 1],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 0, 1, 0], [1, 2, 3, 4, 5]], [1], [3], [5]],
                [None, 0, 0, 0],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[1, 1, 0], [0, 5, 6]], [6], [5], [100]],
                [None, 1, 1, 1],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[3, 3, 3, 3], [10, 20, 30, 40]], [15], [35], [40]],
                [None, 3, 3, 3],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 0], [0, 500000000, 1000000000]], [499999999], [500000000], [1000000000]],
                [None, 0, 1, 0],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 0, 1], [0, 7, 8]], [6], [7], [8]],
                [None, 0, 0, 0],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[1, 0, 1], [2, 4, 6]], [3], [5], [6]],
                [None, 1, 0, 1],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 2, 3, 4], [1, 2, 3, 4, 5]], [2], [4], [5]],
                [None, 1, 3, 4],
            ),
            (
                ["TopVotedCandidate", "q", "q", "q"],
                [[[0, 1, 0, 1, 1], [1, 2, 3, 4, 5]], [1], [3], [5]],
                [None, 0, 0, 1],
            ),
            (["TopVotedCandidate", "q"], [[[0, 1, 1, 0], [0, 1, 2, 3]], [3]], [None, 0]),
            (
                ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"],
                [[[0, 0, 0, 1, 1, 1], [1, 3, 5, 7, 9, 11]], [2], [4], [6], [8], [10], [12]],
                [None, 0, 0, 0, 0, 0, 1],
            ),
        ],
    )
    def test_online_election(
        self, operations: list[str], inputs: list[list], expected: list[int | None]
    ):
        result, _ = run_online_election(TopVotedCandidate, operations, inputs)
        assert_online_election(result, expected)
