import pytest

from leetcode_py import logged_test

from .helpers import assert_find_ladders, run_find_ladders
from .solution import Solution


class TestWordLadderII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "begin_word, end_word, word_list, expected",
        [
            (
                "hit",
                "cog",
                ["hot", "dot", "dog", "lot", "log", "cog"],
                [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
            ),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
            ("hot", "dot", ["dot"], [["hot", "dot"]]),
            ("hot", "dot", [], []),
            ("hot", "dog", ["hot", "dog"], []),
            ("hot", "dog", ["hot", "hog", "dog"], [["hot", "hog", "dog"]]),
            ("a", "c", ["a", "b", "c"], [["a", "c"]]),
            ("aa", "bb", ["ab", "ba", "bb"], [["aa", "ba", "bb"], ["aa", "ab", "bb"]]),
            ("aa", "ad", ["ab", "ac", "ad"], [["aa", "ad"]]),
            (
                "lost",
                "miss",
                ["most", "mist", "miss", "lost", "fist", "fish"],
                [["lost", "most", "mist", "miss"]],
            ),
            ("hit", "cog", ["hot", "dot", "dog", "cog"], [["hit", "hot", "dot", "dog", "cog"]]),
            ("hot", "dot", ["hot", "dot"], [["hot", "dot"]]),
            ("ab", "ba", ["ab", "bb", "cb", "ba"], [["ab", "bb", "ba"]]),
            ("aa", "cc", ["ab", "ac", "bb", "bc", "cc"], [["aa", "ac", "cc"]]),
            ("red", "tax", ["ted", "tex", "red", "tax"], [["red", "ted", "tex", "tax"]]),
            ("bc", "ac", ["ab", "ac", "ba", "cb", "cc"], [["bc", "ac"]]),
            ("cb", "aa", ["aa", "ac", "bc", "cc"], [["cb", "cc", "ac", "aa"]]),
            ("cc", "bb", ["ab", "bb", "bc", "ca", "cb"], [["cc", "bc", "bb"], ["cc", "cb", "bb"]]),
            ("bb", "cc", ["ab", "cb", "cc"], [["bb", "cb", "cc"]]),
            ("ac", "ab", ["aa", "ab", "bc", "cb", "cc"], [["ac", "ab"]]),
            ("cc", "ac", ["ab", "ac", "ba"], [["cc", "ac"]]),
            (
                "ac",
                "ba",
                ["aa", "ac", "ba", "bb", "bc", "cc"],
                [["ac", "bc", "ba"], ["ac", "aa", "ba"]],
            ),
            ("cb", "ab", ["ab", "ac", "ba", "bc", "cb"], [["cb", "ab"]]),
        ],
    )
    def test_find_ladders(
        self, begin_word: str, end_word: str, word_list: list[str], expected: list[list[str]]
    ):
        result = run_find_ladders(Solution, begin_word, end_word, word_list)
        assert_find_ladders(result, expected)
