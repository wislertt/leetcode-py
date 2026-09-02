import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_cost, run_minimum_cost
from .solution import Solution


class TestMinimumCostToConvertStringI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "source, target, original, changed, cost, expected",
        [
            (
                "abcd",
                "acbe",
                ["a", "b", "c", "c", "e", "d"],
                ["b", "c", "b", "e", "b", "e"],
                [2, 5, 5, 1, 2, 20],
                28,
            ),
            ("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2], 12),
            ("abcd", "abce", ["a"], ["e"], [10000], -1),
            ("a", "a", ["b"], ["a"], [1], 0),
            ("a", "b", ["a"], ["b"], [5], 5),
            ("a", "c", ["a", "b"], ["b", "c"], [10, 1], 11),
            ("a", "b", ["a", "a"], ["c", "b"], [3, 10], 10),
            ("a", "c", ["a", "b"], ["b", "d"], [1, 1], -1),
            ("ab", "ba", ["a", "a", "b"], ["b", "b", "a"], [4, 2, 3], 5),
            ("a", "d", ["a", "b", "c"], ["b", "c", "d"], [1, 1, 1], 3),
            ("a", "z", ["a", "b", "a", "m"], ["b", "z", "m", "z"], [100, 100, 1, 1], 2),
            ("a", "m", ["a", "n", "m"], ["b", "a", "n"], [1, 1, 1], -1),
            ("a", "b", ["a", "a", "b"], ["b", "c", "a"], [9, 1, 1], 9),
            ("a", "b", ["a", "a"], ["b", "b"], [7, 3], 3),
            ("a", "b", ["a"], ["b"], [1000000], 1000000),
            ("xyz", "zyx", ["x", "y", "z", "z"], ["y", "z", "x", "a"], [2, 3, 4, 1], 9),
            (
                "ttka",
                "nrxt",
                ["j", "k", "p", "p", "o", "d", "z"],
                ["p", "q", "w", "g", "t", "o", "c"],
                [6, 34, 35, 4, 3, 37, 9],
                -1,
            ),
            (
                "bgft",
                "sihs",
                ["e", "m", "a", "g", "y", "a", "z"],
                ["f", "c", "s", "f", "m", "z", "q"],
                [43, 35, 3, 41, 38, 15, 33],
                -1,
            ),
            (
                "oifl",
                "nwte",
                ["a", "l", "l", "t", "u", "d", "q", "o", "j", "d", "v", "u"],
                ["q", "k", "o", "n", "g", "z", "w", "p", "s", "h", "w", "x"],
                [32, 26, 48, 27, 21, 29, 8, 31, 43, 1, 25, 12],
                -1,
            ),
            (
                "vmqo",
                "lgqe",
                ["l", "m", "w", "o", "m", "i", "e", "f"],
                ["o", "v", "s", "f", "w", "f", "c", "z"],
                [14, 27, 49, 17, 23, 20, 47, 24],
                -1,
            ),
            ("mckj", "qquj", ["f", "t", "m"], ["r", "r", "t"], [42, 5, 19], -1),
            (
                "ftpk",
                "wyjm",
                ["h", "l", "m", "n", "n", "x", "q", "r", "f", "m", "r", "p"],
                ["p", "a", "i", "v", "g", "s", "b", "g", "k", "a", "c", "l"],
                [33, 10, 30, 5, 28, 44, 40, 6, 4, 26, 49, 7],
                -1,
            ),
        ],
    )
    def test_minimum_cost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
        expected: int,
    ):
        result = run_minimum_cost(Solution, source, target, original, changed, cost)
        assert_minimum_cost(result, expected)
