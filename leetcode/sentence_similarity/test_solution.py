import pytest

from leetcode_py import logged_test

from .helpers import assert_are_sentences_similar, run_are_sentences_similar
from .solution import Solution


class TestSentenceSimilarity:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence1, sentence2, similar_pairs, expected",
        [
            (
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "fine"], ["drama", "acting"], ["skills", "talent"]],
                True,
            ),
            (["great"], ["great"], [], True),
            (["great"], ["doubleplus", "good"], [["great", "doubleplus"]], False),
            (["a"], ["b"], [["a", "b"]], True),
            (["a"], ["b"], [], False),
            (["a", "b"], ["a", "c"], [["b", "c"]], True),
            (["a", "b"], ["b", "a"], [], False),
            (["I", "am", "happy"], ["I", "am", "sad"], [["happy", "sad"], ["sad", "happy"]], True),
            (["x"], ["x"], [["x", "y"], ["y", "x"]], True),
            (["a", "b", "c"], ["a", "b"], [], False),
            (["ab", "cd"], ["ef", "gh"], [["ab", "ef"], ["cd", "gh"], ["gh", "cd"]], True),
            (["a", "b"], ["c", "d"], [["a", "c"], ["b", "e"]], False),
            (
                ["one", "two"],
                ["uno", "dos"],
                [["one", "uno"], ["two", "dos"], ["dos", "two"]],
                True,
            ),
            (["hi"], ["hi"], [["hi", "hello"]], True),
        ],
    )
    def test_are_sentences_similar(
        self,
        sentence1: list[str],
        sentence2: list[str],
        similar_pairs: list[list[str]],
        expected: bool,
    ):
        result = run_are_sentences_similar(Solution, sentence1, sentence2, similar_pairs)
        assert_are_sentences_similar(result, expected)
