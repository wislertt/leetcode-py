import pytest

from leetcode_py import logged_test

from .helpers import assert_winner_of_game, run_winner_of_game
from .solution import Solution


class TestRemoveColoredPiecesIfBothNeighborsAreTheSameColor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "colors, expected",
        [
            ("AAABABB", True),
            ("AA", False),
            ("ABBBBBBBAAA", False),
            ("A", False),
            ("B", False),
            ("BB", False),
            ("AAA", True),
            ("BBB", False),
            ("AB", False),
            ("ABAB", False),
            ("AAAA", True),
            ("BBBB", False),
            ("AAABBB", False),
            ("BBBAAA", False),
            ("AAAAA", True),
            ("BBBBB", False),
            ("AAABBBB", False),
            ("AAAABBBB", False),
            ("BAAA", True),
            ("ABABAB", False),
            ("AABBBBBAB", False),
            ("ABBABBBABBAAA", False),
            ("AABBBABBB", False),
            ("BAABAAABAABAAABB", True),
            ("BBABABABBAABABAA", False),
            ("AAABBAABBABBAB", True),
            ("BBBBBBABBAAAB", False),
            ("BBAAABBAAABABA", True),
        ],
    )
    def test_winner_of_game(self, colors: str, expected: bool):
        result = run_winner_of_game(Solution, colors)
        assert_winner_of_game(result, expected)
