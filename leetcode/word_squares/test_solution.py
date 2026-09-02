import pytest

from leetcode_py import logged_test

from .helpers import assert_word_squares, assert_word_squares_solution_count, run_word_squares
from .solution import Solution


class TestWordSquares:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (
                ["area", "lead", "wall", "lady", "ball"],
                [["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]],
            ),
            (
                ["abat", "baba", "atan", "atal"],
                [["baba", "abat", "baba", "atal"], ["baba", "abat", "baba", "atan"]],
            ),
            (["ab", "ba"], [["ab", "ba"], ["ba", "ab"]]),
            (["a"], [["a"]]),
            (["ab"], []),
            (["ab", "cd"], []),
        ],
    )
    def test_word_squares(self, words: list[str], expected: list[list[str]]):
        result = run_word_squares(Solution, words)
        assert_word_squares(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "words, expected_count",
        [
            (["area", "lead", "wall", "lady", "ball"], 2),
            (["abat", "baba", "atan", "atal"], 2),
            (["ab", "ba"], 2),
            (["b", "a"], 2),
            (["abcd", "bnrt", "crmy", "dtye", "dvke"], 1),
            (["ab", "ba", "aa"], 5),
        ],
    )
    def test_word_squares_solution_count(self, words: list[str], expected_count: int):
        result = run_word_squares(Solution, words)
        assert_word_squares_solution_count(result, expected_count)
