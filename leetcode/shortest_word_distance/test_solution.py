import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_distance, run_shortest_distance
from .solution import Solution


class TestShortestWordDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words_dict, word1, word2, expected",
        [
            (["practice", "makes", "perfect", "coding", "makes"], "coding", "practice", 3),
            (["practice", "makes", "perfect", "coding", "makes"], "makes", "coding", 1),
            (["a", "x", "x", "b"], "a", "b", 3),
            (["a", "x", "b", "x", "a"], "a", "b", 2),
            (["a", "b", "c", "d", "e"], "a", "e", 4),
            (["b", "a", "c", "d", "e", "a"], "b", "e", 4),
            (["w", "x", "y", "z", "w"], "w", "y", 2),
            (["q", "a", "b", "c", "d", "e", "f", "q", "r"], "q", "r", 1),
            (["a", "b", "a", "b", "a", "b", "a", "b", "a"], "a", "b", 1),
            (["cat", "dog", "bird", "fish", "cat", "dog"], "cat", "fish", 1),
            (["a", "z", "y", "x", "w", "v", "u", "t", "b"], "a", "b", 8),
            (["red", "blue", "red", "green", "blue", "red"], "red", "green", 1),
            (["i", "j", "k", "i", "j", "k", "i", "j", "k"], "i", "j", 1),
            (["one", "two", "three", "four", "five", "one"], "one", "five", 1),
            (["x1", "y2", "x3", "y4", "x5", "y6", "x7", "y8", "x9"], "x1", "x9", 8),
        ],
    )
    def test_shortest_distance(self, words_dict: list[str], word1: str, word2: str, expected: int):
        result = run_shortest_distance(Solution, words_dict, word1, word2)
        assert_shortest_distance(result, expected)
