import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_word_distance_ii, run_shortest_word_distance_ii
from .solution import WordDistance


class TestShortestWordDistanceII:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["WordDistance", "shortest", "shortest"],
                [
                    ["practice", "makes", "perfect", "coding", "makes"],
                    ["coding", "practice"],
                    ["makes", "coding"],
                ],
                [None, 3, 1],
            ),
            (["WordDistance", "shortest"], [["a", "b"], ["a", "b"]], [None, 1]),
            (
                ["WordDistance", "shortest", "shortest"],
                [["a", "b", "a"], ["a", "b"], ["b", "a"]],
                [None, 1, 1],
            ),
            (["WordDistance", "shortest"], [["x", "y", "z", "x"], ["x", "z"]], [None, 1]),
            (
                ["WordDistance", "shortest", "shortest"],
                [["a", "b", "c", "d", "e", "f", "a"], ["a", "f"], ["a", "b"]],
                [None, 1, 1],
            ),
            (
                ["WordDistance", "shortest", "shortest"],
                [["aa", "bb", "aa", "bb", "aa"], ["aa", "bb"], ["bb", "aa"]],
                [None, 1, 1],
            ),
            (
                ["WordDistance", "shortest"],
                [["hello", "world", "leetcode", "hello", "world"], ["hello", "world"]],
                [None, 1],
            ),
            (
                ["WordDistance", "shortest", "shortest"],
                [["a", "b", "a", "b", "a", "b", "a"], ["a", "b"], ["b", "a"]],
                [None, 1, 1],
            ),
            (
                ["WordDistance", "shortest", "shortest", "shortest"],
                [
                    ["one", "two", "three", "two", "one", "three"],
                    ["one", "three"],
                    ["two", "three"],
                    ["one", "two"],
                ],
                [None, 1, 1, 1],
            ),
            (
                ["WordDistance", "shortest"],
                [["m", "n", "o", "p", "q", "r", "n", "m"], ["m", "n"]],
                [None, 1],
            ),
            (
                ["WordDistance", "shortest", "shortest", "shortest"],
                [
                    ["practice", "makes", "perfect", "coding", "makes"],
                    ["practice", "coding"],
                    ["perfect", "makes"],
                    ["coding", "makes"],
                ],
                [None, 3, 1, 1],
            ),
            (
                ["WordDistance", "shortest", "shortest"],
                [["a", "b", "c", "a", "b"], ["c", "b"], ["a", "c"]],
                [None, 1, 1],
            ),
            (["WordDistance", "shortest"], [["q", "p", "q", "p", "q", "p"], ["p", "q"]], [None, 1]),
        ],
    )
    def test_shortest_word_distance_ii(
        self, operations: list[str], inputs: list[list[str]], expected: list[int | None]
    ):
        result, _ = run_shortest_word_distance_ii(WordDistance, operations, inputs)
        assert_shortest_word_distance_ii(result, expected)
