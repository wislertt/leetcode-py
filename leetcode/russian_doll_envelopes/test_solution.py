import pytest

from leetcode_py import logged_test

from .helpers import assert_max_envelopes, run_max_envelopes
from .solution import Solution


class TestRussianDollEnvelopes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "envelopes, expected",
        [
            ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
            ([[1, 1], [1, 1], [1, 1]], 1),
            ([[1, 1]], 1),
            ([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]], 3),
            ([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]], 4),
            ([[10, 8], [1, 12], [6, 15], [2, 18]], 2),
            ([[5, 4], [6, 4], [6, 7], [2, 3], [1, 2], [8, 9], [7, 8]], 6),
            ([[1, 2], [2, 3], [3, 4], [4, 5]], 4),
            ([[2, 100], [3, 200], [4, 300], [5, 250], [5, 400], [5, 500], [6, 360], [7, 380]], 5),
            (
                [[17, 15], [17, 25], [5, 3], [17, 11], [1, 1], [4, 11], [19, 3], [9, 10], [14, 16]],
                5,
            ),
            ([[100000, 100000], [99999, 99999], [1, 1]], 3),
            ([[1, 1], [2, 2], [2, 3], [3, 4], [3, 5], [4, 6]], 4),
            (
                [[15, 8], [2, 20], [5, 3], [2, 14], [18, 2], [8, 18], [18, 14], [16, 18], [15, 17]],
                3,
            ),
            ([[2, 1], [4, 1], [6, 2], [8, 3], [10, 5], [12, 8], [14, 13], [16, 21]], 7),
            ([[1, 100], [2, 99], [3, 98], [4, 97]], 1),
        ],
    )
    def test_max_envelopes(self, envelopes: list[list[int]], expected: int):
        result = run_max_envelopes(Solution, envelopes)
        assert_max_envelopes(result, expected)
