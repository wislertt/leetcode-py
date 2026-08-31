import pytest

from leetcode_py import logged_test

from .helpers import assert_k_inverse_pairs, run_k_inverse_pairs
from .solution import Solution


class TestKInversePairsArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (3, 0, 1),
            (3, 1, 2),
            (1, 0, 1),
            (2, 1, 1),
            (4, 6, 1),
            (1000, 1, 999),
            (1000, 0, 1),
            (10, 5, 1068),
            (4, 0, 1),
            (5, 3, 15),
            (6, 3, 29),
            (7, 4, 98),
            (50, 100, 881835314),
            (100, 200, 976500783),
            (1000, 1000, 663677020),
        ],
    )
    def test_k_inverse_pairs(self, n: int, k: int, expected: int):
        result = run_k_inverse_pairs(Solution, n, k)
        assert_k_inverse_pairs(result, expected)
