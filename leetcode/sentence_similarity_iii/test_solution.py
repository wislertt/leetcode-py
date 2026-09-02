import pytest

from leetcode_py import logged_test

from .helpers import assert_are_sentences_similar, run_are_sentences_similar
from .solution import Solution


class TestSentenceSimilarityIii:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence1, sentence2, expected",
        [
            ("My name is Haley", "My Haley", True),
            ("of", "A lot of words", False),
            ("Eating right now", "Eating", True),
            ("Hello Jane", "Hello my name is Jane", True),
            ("Frog cool", "Frogs are cool", False),
            ("a", "a", True),
            ("a", "b", False),
            ("A", "a", False),
            ("one two three", "one three", True),
            ("one two three four", "one three four", True),
            ("here", "long sentence here", True),
            ("x y z", "y z x", False),
            ("b b", "b", True),
            ("a b c", "a a b c", True),
            ("Cauldron is so cool", "Cauldron", True),
            ("C", "C", True),
            ("alpha beta gamma", "alpha", True),
            ("big red", "big red", True),
            ("start mid end", "start end", True),
            ("p q r s", "p r s", True),
            ("a x b y c", "a b c", False),
            ("ab", "a b", False),
            ("one two", "two one", False),
            ("ca ab b abc", "b ca bc b c b", False),
            ("c ca ab", "b b ca ab", False),
            ("ca a ca ca ab a", "a abc b a bc abc", False),
            ("abc abc c bc", "abc ca", False),
            ("a bc a abc", "bc ca a ca", False),
        ],
    )
    def test_are_sentences_similar(self, sentence1: str, sentence2: str, expected: bool):
        result = run_are_sentences_similar(Solution, sentence1, sentence2)
        assert_are_sentences_similar(result, expected)
