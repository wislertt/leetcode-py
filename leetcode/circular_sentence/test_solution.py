import pytest

from leetcode_py import logged_test

from .helpers import assert_is_circular_sentence, run_is_circular_sentence
from .solution import Solution


class TestCircularSentence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence, expected",
        [
            ("leetcode exercises sound delightful", True),
            ("eetcode", True),
            ("Leetcode is cool", False),
            ("hello world hello world", False),
            ("a", True),
            ("ab", False),
            ("aa", True),
            ("aba", True),
            ("happy Leetcode", False),
            ("I like Leetcode", False),
            ("leetcode eats soul", True),
            ("HELLO", False),
            ("ab ba", True),
            ("abc cba", True),
            ("aaa aaa", True),
            ("ab cd", False),
            ("xyz zyx", True),
            ("Ala", False),
            ("Leetcode", False),
            ("aeiou uoiea", True),
            ("snake elixir ruin nice", False),
            ("nice lace echo onion", False),
            ("qbbjqnc c cbbijjb", False),
            ("l l", True),
            ("l ltb blu", False),
            ("niyh hctks shpaq", False),
            ("wjmpi iy ynfcr r ra", False),
            ("jr rd d dczjrd", False),
            ("pd", False),
            ("q q", True),
        ],
    )
    def test_is_circular_sentence(self, sentence: str, expected: bool):
        result = run_is_circular_sentence(Solution, sentence)
        assert_is_circular_sentence(result, expected)
