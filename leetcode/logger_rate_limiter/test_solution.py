import pytest

from leetcode_py import logged_test

from .helpers import assert_logger_rate_limiter, run_logger_rate_limiter
from .solution import Logger


class TestLoggerRateLimiter:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]],
                [None, True, True, False, False, False, True],
            ),
            (
                ["Logger", "should_print_message", "should_print_message"],
                [[], [5, "a"], [5, "a"]],
                [None, True, False],
            ),
            (
                ["Logger", "should_print_message", "should_print_message"],
                [[], [0, "x"], [10, "x"]],
                [None, True, True],
            ),
            (
                ["Logger", "should_print_message", "should_print_message"],
                [[], [0, "x"], [9, "x"]],
                [None, True, False],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [1, "a"], [1, "b"], [1, "c"], [1, "a"]],
                [None, True, True, True, False],
            ),
            (
                ["Logger", "should_print_message", "should_print_message"],
                [[], [0, "m"], [100, "m"]],
                [None, True, True],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [2, "p"], [11, "q"], [12, "p"], [21, "q"]],
                [None, True, True, True, True],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [0, "a"], [10, "a"], [20, "a"], [30, "a"]],
                [None, True, True, True, True],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [7, "rogue"], [7, "rogue"], [17, "rogue"], [16, "rogue"]],
                [None, True, False, True, False],
            ),
            (
                ["Logger", "should_print_message", "should_print_message", "should_print_message"],
                [[], [0, "ab"], [0, "ab"], [1, "ab"]],
                [None, True, False, False],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [3, "z"], [13, "z"], [12, "z"], [23, "z"]],
                [None, True, True, False, True],
            ),
            (
                [
                    "Logger",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                    "should_print_message",
                ],
                [[], [100, "hit"], [100, "hit"], [110, "hit"], [109, "hit"], [110, "hit"]],
                [None, True, False, True, False, False],
            ),
        ],
    )
    def test_logger_rate_limiter(
        self, operations: list[str], inputs: list[list], expected: list[bool | None]
    ):
        result, _ = run_logger_rate_limiter(Logger, operations, inputs)
        assert_logger_rate_limiter(result, expected)
