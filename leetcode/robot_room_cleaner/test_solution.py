import pytest

from leetcode_py import logged_test

from .helpers import assert_clean_room, run_clean_room
from .solution import Solution


class TestRobotRoomCleaner:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "room, row, col, expected",
        [
            (
                [
                    [1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                ],
                1,
                3,
                30,
            ),
            ([[1]], 0, 0, 1),
            ([[1, 1], [1, 0]], 0, 0, 3),
            ([[0, 1], [1, 1]], 0, 1, 3),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 9),
            ([[1, 0], [0, 0]], 0, 0, 1),
            ([[1, 1, 1, 1]], 0, 1, 4),
            ([[1], [1], [1]], 0, 0, 3),
            ([[1, 1, 0], [0, 1, 1], [1, 1, 1]], 0, 0, 7),
            ([[1, 1], [1, 1], [1, 1], [1, 1]], 2, 1, 8),
            (
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1],
                    [0, 1, 0, 1, 1],
                    [0, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                ],
                0,
                0,
                17,
            ),
            (
                [
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                0,
                0,
                23,
            ),
            (
                [
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 1],
                ],
                0,
                0,
                21,
            ),
            (
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1],
                    [1, 0, 1, 1, 0],
                    [1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1],
                ],
                0,
                0,
                19,
            ),
        ],
    )
    def test_clean_room(self, room: list[list[int]], row: int, col: int, expected: int):
        result = run_clean_room(Solution, room, row, col)
        assert_clean_room(result, expected)
