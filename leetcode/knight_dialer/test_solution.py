import pytest

from leetcode_py import logged_test

from .helpers import assert_knight_dialer, run_knight_dialer
from .solution import Solution


class TestKnightDialer:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 10),
            (2, 20),
            (3, 46),
            (4, 104),
            (5, 240),
            (6, 544),
            (7, 1256),
            (8, 2848),
            (9, 6576),
            (10, 14912),
            (12, 78080),
            (15, 944000),
            (20, 58689536),
            (100, 540641702),
            (1000, 88106097),
            (3131, 136006598),
            (5000, 406880451),
        ],
    )
    def test_knight_dialer(self, n: int, expected: int):
        result = run_knight_dialer(Solution, n)
        assert_knight_dialer(result, expected)
