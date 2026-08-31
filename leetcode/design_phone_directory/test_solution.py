import pytest

from leetcode_py import logged_test

from .helpers import assert_phone_directory, run_phone_directory
from .solution import PhoneDirectory


class TestDesignPhoneDirectory:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"],
                [[3], [], [], [2], [], [2], [2], [2]],
                [None, 0, 1, True, 2, False, None, True],
            ),
            (["PhoneDirectory", "get", "get"], [[1], [], []], [None, 0, -1]),
            (
                ["PhoneDirectory", "check", "get", "check", "check"],
                [[2], [1], [], [1], [0]],
                [None, True, 0, True, False],
            ),
            (
                ["PhoneDirectory", "get", "get", "release", "get", "check"],
                [[2], [], [], [0], [], [0]],
                [None, 0, 1, None, 0, False],
            ),
            (
                ["PhoneDirectory", "get", "get", "get", "release", "get", "release", "get"],
                [[3], [], [], [], [1], [], [0], []],
                [None, 0, 1, 2, None, 1, None, 0],
            ),
            (
                ["PhoneDirectory", "get", "check", "get", "release", "check", "get", "check"],
                [[5], [], [3], [], [0], [0], [], [0]],
                [None, 0, True, 1, None, True, 2, True],
            ),
            (
                [
                    "PhoneDirectory",
                    "get",
                    "get",
                    "get",
                    "get",
                    "get",
                    "release",
                    "release",
                    "get",
                    "get",
                    "get",
                ],
                [[4], [], [], [], [], [], [3], [1], [], [], []],
                [None, 0, 1, 2, 3, -1, None, None, 3, 1, -1],
            ),
            (
                ["PhoneDirectory", "get", "release", "get", "check", "release", "get"],
                [[2], [], [0], [], [0], [1], []],
                [None, 0, None, 1, True, None, 0],
            ),
            (
                ["PhoneDirectory", "check", "check", "get", "get", "get", "check"],
                [[3], [0], [2], [], [], [], [1]],
                [None, True, True, 0, 1, 2, False],
            ),
            (
                [
                    "PhoneDirectory",
                    "get",
                    "get",
                    "release",
                    "release",
                    "get",
                    "get",
                    "get",
                    "check",
                ],
                [[6], [], [], [1], [0], [], [], [], [4]],
                [None, 0, 1, None, None, 2, 3, 4, False],
            ),
            (
                ["PhoneDirectory", "get", "release", "check", "release", "check"],
                [[3], [], [0], [0], [1], [2]],
                [None, 0, None, True, None, True],
            ),
            (
                [
                    "PhoneDirectory",
                    "check",
                    "get",
                    "get",
                    "release",
                    "release",
                    "get",
                    "get",
                    "get",
                    "check",
                ],
                [[4], [0], [], [], [0], [1], [], [], [], [3]],
                [None, True, 0, 1, None, None, 2, 3, 0, False],
            ),
            (
                [
                    "PhoneDirectory",
                    "get",
                    "get",
                    "check",
                    "release",
                    "get",
                    "check",
                    "get",
                    "get",
                    "get",
                ],
                [[5], [], [], [4], [0], [], [0], [], [], []],
                [None, 0, 1, True, None, 2, True, 3, 4, 0],
            ),
        ],
    )
    def test_phone_directory(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | bool | None]
    ):
        result, _ = run_phone_directory(PhoneDirectory, operations, inputs)
        assert_phone_directory(result, expected)
