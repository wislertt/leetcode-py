import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_find_strobogrammatic,
    assert_find_strobogrammatic_count,
    run_find_strobogrammatic,
)
from .solution import Solution


class TestStrobogrammaticNumberII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, ["0", "1", "8"]),
            (2, ["11", "69", "88", "96"]),
            (
                3,
                [
                    "101",
                    "111",
                    "181",
                    "609",
                    "619",
                    "689",
                    "808",
                    "818",
                    "888",
                    "906",
                    "916",
                    "986",
                ],
            ),
            (
                4,
                [
                    "1001",
                    "1111",
                    "1691",
                    "1881",
                    "1961",
                    "6009",
                    "6119",
                    "6699",
                    "6889",
                    "6969",
                    "8008",
                    "8118",
                    "8698",
                    "8888",
                    "8968",
                    "9006",
                    "9116",
                    "9696",
                    "9886",
                    "9966",
                ],
            ),
        ],
    )
    def test_find_strobogrammatic(self, n: int, expected: list[str]):
        result = run_find_strobogrammatic(Solution, n)
        assert_find_strobogrammatic(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "n, expected_count",
        [
            (5, 60),
            (6, 100),
            (7, 300),
            (8, 500),
            (9, 1500),
            (10, 2500),
            (11, 7500),
            (12, 12500),
            (13, 37500),
            (14, 62500),
        ],
    )
    def test_find_strobogrammatic_count(self, n: int, expected_count: int):
        result = run_find_strobogrammatic(Solution, n)
        assert_find_strobogrammatic_count(result, expected_count)
