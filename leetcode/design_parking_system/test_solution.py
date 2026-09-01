import pytest

from leetcode_py import logged_test

from .helpers import assert_parking_system, run_parking_system
from .solution import ParkingSystem


class TestDesignParkingSystem:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
                    [[1, 1, 0], [1], [2], [3], [1]],
                    [None, True, True, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car"],
                    [[0, 0, 0], [1], [2], [3]],
                    [None, False, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car", "add_car"],
                    [[1, 0, 1], [1], [1], [3], [3], [2]],
                    [None, True, False, True, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
                    [[1000, 1000, 1000], [2], [2], [2], [2]],
                    [None, True, True, True, True],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
                    [[3, 0, 0], [1], [1], [1], [1]],
                    [None, True, True, True, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[2, 2, 2], [3], [1], [2], [3], [1], [2], [1]],
                    [None, True, True, True, True, True, True, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
                    [[0, 1, 1], [1], [2], [3], [2]],
                    [None, False, True, True, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[1, 1, 1], [1], [2], [3], [1], [2], [3]],
                    [None, True, True, True, False, False, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[2, 0, 2], [1], [3], [3], [3], [3], [2]],
                    [None, True, True, True, False, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car"],
                    [[0, 0, 1], [3], [1], [1], [2]],
                    [None, True, False, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car", "add_car"],
                    [[1, 2, 0], [1], [3], [3], [3], [1]],
                    [None, True, False, False, False, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[0, 2, 2], [3], [3], [2], [1], [2], [3]],
                    [None, True, True, True, False, True, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[1, 2, 1], [2], [2], [3], [2], [2], [3]],
                    [None, True, True, True, False, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car"],
                    [[1, 0, 2], [1], [2], [2]],
                    [None, True, False, False],
                )
            ),
            (
                (
                    [
                        "ParkingSystem",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                        "add_car",
                    ],
                    [[1, 1, 0], [3], [1], [3], [1], [1], [1]],
                    [None, False, True, False, False, False, False],
                )
            ),
            (
                (
                    ["ParkingSystem", "add_car", "add_car", "add_car", "add_car", "add_car"],
                    [[1, 1, 2], [1], [1], [1], [2], [3]],
                    [None, True, False, False, True, True],
                )
            ),
        ],
    )
    def test_parking_system(
        self, operations: list[str], inputs: list[list[int]], expected: list[bool | None]
    ):
        result, _ = run_parking_system(ParkingSystem, operations, inputs)
        assert_parking_system(result, expected)
