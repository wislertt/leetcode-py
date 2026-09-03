import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_tic_tac_toe, run_valid_tic_tac_toe
from .solution import Solution


class TestValidTicTacToeState:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, expected",
        [
            (["   ", "   ", "   "], True),
            (["O  ", "   ", "   "], False),
            (["XOX", " X ", "   "], False),
            (["XOX", "O O", "XOX"], True),
            (["XXX", "OO ", "   "], True),
            (["X  ", "X O", "X O"], True),
            (["X  ", "OX ", " OX"], True),
            (["O X", " X ", "XO "], True),
            (["XX ", "OOO", "  X"], True),
            (["OX ", "OX ", "O X"], True),
            (["OXX", "XO ", "  O"], True),
            (["XOX", "OXO", "XOX"], True),
            (["XXX", "OOO", "   "], False),
            (["XXX", "OO ", "O  "], False),
            (["OOO", "XX ", "XX "], False),
            (["XX ", "XX ", "   "], False),
            (["XOX", "XOX", "X  "], False),
            (["O X", "X O", "  X"], True),
            ([" X ", "  O", "XO "], True),
            (["X X", "X O", "OOX"], True),
            (["XO ", "X X", "XX "], False),
            (["O O", " XX", "O O"], False),
            (["OOO", "X O", "OX "], False),
            (["OOX", "XXX", "OX "], False),
        ],
    )
    def test_valid_tic_tac_toe(self, board: list[str], expected: bool):
        result = run_valid_tic_tac_toe(Solution, board)
        assert_valid_tic_tac_toe(result, expected)
