import pytest

from leetcode_py import logged_test

from .helpers import assert_generate_sentences, run_generate_sentences
from .solution import Solution


class TestSynonymousSentences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "synonyms, text, expected",
        [
            (
                [["a", "b"], ["c", "d"], ["b", "e"]],
                "a c",
                ["a c", "a d", "b c", "b d", "e c", "e d"],
            ),
            ([["a", "b"], ["c", "d"]], "a c", ["a c", "a d", "b c", "b d"]),
            ([], "a b", ["a b"]),
            ([["a", "b"]], "a", ["a", "b"]),
            ([["a", "b"], ["b", "c"], ["c", "d"]], "a x", ["a x", "b x", "c x", "d x"]),
            ([["a", "b"]], "z a z", ["z a z", "z b z"]),
            ([["a", "b"]], "a a", ["a a", "a b", "b a", "b b"]),
            ([["A", "b"]], "A b", ["A A", "A b", "b A", "b b"]),
            ([["a", "b"]], "c d", ["c d"]),
            ([["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]], "a", ["a", "b", "c", "d", "e"]),
            ([["a", "b"], ["c", "d"], ["e", "f"]], "a", ["a", "b"]),
            ([["big", "large"], ["small", "tiny"]], "big", ["big", "large"]),
            ([["x", "y"]], "a b c x y", ["a b c x x", "a b c x y", "a b c y x", "a b c y y"]),
            ([["m", "n"], ["o", "p"]], "n o", ["m o", "m p", "n o", "n p"]),
            ([["a", "b"], ["a", "c"]], "b x", ["a x", "b x", "c x"]),
            ([["a", "b"], ["c", "d"]], "a c z", ["a c z", "a d z", "b c z", "b d z"]),
            ([["a", "b"], ["c", "b"]], "c z", ["a z", "b z", "c z"]),
            ([["one", "uno"]], "one x", ["one x", "uno x"]),
            ([["ab", "cd"], ["ef", "gh"]], "ab ef", ["ab ef", "ab gh", "cd ef", "cd gh"]),
            ([["happy", "joy"]], "happy today sad", ["happy today sad", "joy today sad"]),
        ],
    )
    def test_generate_sentences(self, synonyms: list[list[str]], text: str, expected: list[str]):
        result = run_generate_sentences(Solution, synonyms, text)
        assert_generate_sentences(result, expected)
