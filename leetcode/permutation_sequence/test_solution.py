import pytest

from leetcode_py import logged_test

from .helpers import assert_get_permutation, run_get_permutation
from .solution import Solution


class TestPermutationSequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (3, 3, "213"),
            (4, 9, "2314"),
            (3, 1, "123"),
            (1, 1, "1"),
            (2, 1, "12"),
            (2, 2, "21"),
            (3, 6, "321"),
            (4, 1, "1234"),
            (4, 24, "4321"),
            (5, 42, "24531"),
            (6, 400, "425361"),
            (7, 500, "1627354"),
            (8, 7777, "25781346"),
            (9, 1, "123456789"),
            (9, 362880, "987654321"),
            (9, 2143, "125984367"),
        ],
    )
    def test_get_permutation(self, n: int, k: int, expected: str):
        result = run_get_permutation(Solution, n, k)
        assert_get_permutation(result, expected)
