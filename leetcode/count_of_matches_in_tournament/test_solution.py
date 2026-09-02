import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_matches, run_number_of_matches
from .solution import Solution


class TestCountOfMatchesInTournament:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 4),
            (6, 5),
            (7, 6),
            (8, 7),
            (9, 8),
            (10, 9),
            (11, 10),
            (12, 11),
            (13, 12),
            (14, 13),
            (15, 14),
            (16, 15),
            (17, 16),
            (18, 17),
            (19, 18),
            (20, 19),
            (21, 20),
            (22, 21),
            (23, 22),
            (24, 23),
            (25, 24),
            (26, 25),
            (27, 26),
            (28, 27),
            (29, 28),
            (30, 29),
            (50, 49),
            (100, 99),
            (101, 100),
            (150, 149),
            (199, 198),
            (200, 199),
        ],
    )
    def test_number_of_matches(self, n: int, expected: int):
        result = run_number_of_matches(Solution, n)
        assert_number_of_matches(result, expected)
