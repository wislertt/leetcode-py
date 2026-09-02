import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_word_distance_iii, run_shortest_word_distance_iii
from .solution import Solution


class TestShortestWordDistanceIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words_dict, word1, word2, expected",
        [
            (["practice", "makes", "perfect", "coding", "makes"], "makes", "coding", 1),
            (["practice", "makes", "perfect", "coding", "makes"], "makes", "makes", 3),
            (["a", "a", "a"], "a", "a", 1),
            (["a", "b"], "a", "b", 1),
            (["b", "a"], "a", "b", 1),
            (["a", "x", "x", "b"], "a", "b", 3),
            (["a", "x", "b", "x", "a"], "a", "b", 2),
            (["cat", "cat", "dog"], "cat", "cat", 1),
            (["cat", "dog", "cat", "dog", "cat"], "cat", "dog", 1),
            (["a", "b", "c", "d", "e"], "e", "a", 4),
            (["w", "x", "y", "z", "w"], "w", "w", 4),
            (["i", "j", "k", "i", "j", "k"], "k", "i", 1),
            (["hello", "world", "hello"], "hello", "hello", 2),
            (["one", "two", "one", "three", "one"], "one", "three", 1),
            (["red", "blue", "red", "green"], "red", "green", 1),
            (["m", "n", "m", "n", "m"], "n", "n", 2),
            (["x", "y", "z"], "x", "z", 2),
            (["aa", "bb", "cc", "aa"], "aa", "cc", 1),
        ],
    )
    def test_shortest_word_distance_iii(
        self, words_dict: list[str], word1: str, word2: str, expected: int
    ):
        result = run_shortest_word_distance_iii(Solution, words_dict, word1, word2)
        assert_shortest_word_distance_iii(result, expected)
