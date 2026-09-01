import pytest

from leetcode_py import logged_test

from .helpers import assert_seat_reservation_manager, run_seat_reservation_manager
from .solution import SeatManager


class TestSeatManager:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "unreserve",
                ],
                [[5], [], [], [2], [], [], [], [], [5]],
                [None, 1, 2, None, 2, 3, 4, 5, None],
            ),
            (["SeatManager", "reserve"], [[1], []], [None, 1]),
            (
                ["SeatManager", "reserve", "unreserve", "reserve"],
                [[1], [], [1], []],
                [None, 1, None, 1],
            ),
            (
                ["SeatManager", "reserve", "unreserve", "reserve", "unreserve", "reserve"],
                [[1], [], [1], [], [1], []],
                [None, 1, None, 1, None, 1],
            ),
            (["SeatManager", "reserve", "reserve", "reserve"], [[3], [], [], []], [None, 1, 2, 3]),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                ],
                [[2], [], [], [1], [2], [], []],
                [None, 1, 2, None, None, 1, 2],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                    "reserve",
                ],
                [[4], [], [1], [], [1], [], [], []],
                [None, 1, None, 1, None, 1, 2, 3],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                    "reserve",
                ],
                [[5], [], [], [], [3], [1], [], [], []],
                [None, 1, 2, 3, None, None, 1, 3, 4],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                ],
                [[3], [], [], [1], [], [2], [], []],
                [None, 1, 2, None, 1, None, 2, 3],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                ],
                [[6], [], [], [2], [1], [], [], [], [], []],
                [None, 1, 2, None, None, 1, 2, 3, 4, 5],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                ],
                [[2], [], [], [1], [], [2], []],
                [None, 1, 2, None, 1, None, 2],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                ],
                [[5], [], [], [], [], [], [5], []],
                [None, 1, 2, 3, 4, 5, None, 5],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                ],
                [[7], [], [], [], [2], [], [3], [], []],
                [None, 1, 2, 3, None, 2, None, 3, 4],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "unreserve",
                    "reserve",
                    "unreserve",
                    "reserve",
                ],
                [[4], [], [], [1], [2], [], [1], []],
                [None, 1, 2, None, None, 1, None, 1],
            ),
            (
                [
                    "SeatManager",
                    "reserve",
                    "reserve",
                    "reserve",
                    "unreserve",
                    "unreserve",
                    "unreserve",
                    "reserve",
                    "reserve",
                    "reserve",
                    "reserve",
                ],
                [[5], [], [], [], [3], [2], [1], [], [], [], []],
                [None, 1, 2, 3, None, None, None, 1, 2, 3, 4],
            ),
        ],
    )
    def test_seat_reservation_manager(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_seat_reservation_manager(SeatManager, operations, inputs)
        assert_seat_reservation_manager(result, expected)
