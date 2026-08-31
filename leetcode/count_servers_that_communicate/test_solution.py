import pytest

from leetcode_py import logged_test

from .helpers import assert_count_servers, run_count_servers
from .solution import Solution


class TestCountServersThatCommunicate:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            [[[1, 0], [0, 1]], 0],
            [[[1, 0], [1, 1]], 3],
            [[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4],
            [[[1]], 0],
            [[[1, 1]], 2],
            [[[1], [1]], 2],
            [[[1, 1], [1, 1]], 4],
            [[[1, 0], [0, 0]], 0],
            [[[1, 1, 1], [0, 0, 0]], 3],
            [[[0, 0], [0, 0]], 0],
            [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], 0],
            [[[1, 0, 1], [0, 1, 0], [1, 0, 1]], 4],
            [[[1, 0, 1, 1, 0]], 3],
            [
                [
                    [0, 0, 1, 0, 1],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 0, 1, 1],
                    [1, 1, 1, 1, 0],
                ],
                12,
            ],
            [[[1, 1, 1], [1, 0, 1], [1, 0, 0], [0, 0, 1], [0, 0, 0]], 7],
            [[[1], [0], [1], [0], [0]], 2],
            [[[0, 1, 1, 1]], 3],
            [[[0, 0], [0, 1], [1, 0]], 0],
        ],
    )
    def test_count_servers(self, grid: list[list[int]], expected: int):
        result = run_count_servers(Solution, grid)
        assert_count_servers(result, expected)
