import pytest

from leetcode_py import logged_test

from .helpers import assert_next_greatest_letter, run_next_greatest_letter
from .solution import Solution


class TestFindSmallestLetterGreaterThanTarget:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "letters, target, expected",
        [
            (["c", "f", "j"], "a", "c"),
            (["c", "f", "j"], "c", "f"),
            (["x", "x", "y", "y"], "z", "x"),
            (["a", "b"], "z", "a"),
            (["a", "b"], "a", "b"),
            (["a", "a", "b", "b"], "a", "b"),
            (["e", "e", "e", "k", "q", "q", "q"], "d", "e"),
            (["e", "e", "e", "k", "q", "q", "q"], "k", "q"),
            (["e", "e", "e", "k", "q", "q", "q"], "q", "e"),
            (["e", "e", "g", "g"], "g", "e"),
            (["a", "z"], "z", "a"),
            (["a", "z"], "y", "z"),
            (["a", "z"], "b", "z"),
            (["b", "y"], "a", "b"),
            (["c", "f", "j"], "j", "c"),
            (["c", "f", "j"], "d", "f"),
            (["a", "m", "m", "z"], "l", "m"),
            (["a", "m", "m", "z"], "z", "a"),
        ],
    )
    def test_next_greatest_letter(self, letters: list[str], target: str, expected: str):
        result = run_next_greatest_letter(Solution, letters, target)
        assert_next_greatest_letter(result, expected)
