import pytest

from leetcode_py import logged_test

from .helpers import assert_are_sentences_similar_two, run_are_sentences_similar_two
from .solution import Solution


class TestSentenceSimilarityII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence1, sentence2, similar_pairs, expected",
        [
            (
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]],
                True,
            ),
            (
                ["I", "love", "leetcode"],
                ["I", "love", "onepiece"],
                [
                    ["manga", "onepiece"],
                    ["platform", "anime"],
                    ["leetcode", "platform"],
                    ["anime", "manga"],
                ],
                True,
            ),
            (
                ["I", "love", "leetcode"],
                ["I", "love", "onepiece"],
                [
                    ["manga", "hunterXhunter"],
                    ["platform", "anime"],
                    ["leetcode", "platform"],
                    ["anime", "manga"],
                ],
                False,
            ),
            (["a"], ["b"], [["a", "b"]], True),
            (["a"], ["b"], [], False),
            (["a", "b"], ["b", "a"], [["a", "c"], ["c", "b"]], True),
            (["great"], ["great"], [], True),
            (
                ["a", "b", "c"],
                ["d", "e", "f"],
                [["a", "d"], ["b", "e"], ["f", "c"], ["c", "x"], ["x", "y"]],
                True,
            ),
            (["a", "b"], ["c", "d"], [["a", "c"], ["x", "d"]], False),
            (
                ["one", "two"],
                ["uno", "dos"],
                [["one", "uno"], ["uno", "ein"], ["two", "dos"], ["ein", "zwei"], ["zwei", "dos"]],
                True,
            ),
            (["x"], ["y"], [["y", "x"]], True),
            (["a", "b"], ["a", "c"], [], False),
            (["a", "b"], ["a", "c"], [["b", "c"]], True),
        ],
    )
    def test_are_sentences_similar_two(
        self,
        sentence1: list[str],
        sentence2: list[str],
        similar_pairs: list[list[str]],
        expected: bool,
    ):
        result = run_are_sentences_similar_two(Solution, sentence1, sentence2, similar_pairs)
        assert_are_sentences_similar_two(result, expected)
