import pytest

from leetcode_py import logged_test

from .helpers import assert_earliest_acq, run_earliest_acq
from .solution import Solution


class TestTheEarliestMomentWhenEveryoneBecomeFriends:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "logs, n, expected",
        [
            (
                [
                    [20190101, 0, 1],
                    [20190104, 3, 4],
                    [20190107, 2, 3],
                    [20190211, 1, 5],
                    [20190224, 2, 4],
                    [20190301, 0, 3],
                    [20190312, 1, 2],
                    [20190322, 4, 5],
                ],
                6,
                20190301,
            ),
            ([[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4, 3),
            ([[1, 0, 1]], 2, 1),
            ([[1, 0, 1], [2, 1, 2]], 3, 2),
            ([[5, 0, 1], [3, 1, 2]], 3, 5),
            ([[1, 0, 1], [2, 2, 3]], 4, -1),
            ([[9, 0, 1], [3, 2, 3], [7, 1, 2]], 4, 9),
            ([[1, 0, 1]], 3, -1),
            ([[100, 0, 1], [200, 1, 2], [300, 2, 3], [400, 3, 0]], 4, 300),
            ([[2, 0, 1], [1, 1, 0]], 2, 1),
            ([[10, 0, 1], [20, 2, 3], [30, 0, 2]], 4, 30),
            ([[0, 0, 1], [1, 1, 2]], 3, 1),
        ],
    )
    def test_earliest_acq(self, logs: list[list[int]], n: int, expected: int):
        result = run_earliest_acq(Solution, logs, n)
        assert_earliest_acq(result, expected)
