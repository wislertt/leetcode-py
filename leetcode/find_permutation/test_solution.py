import pytest

from leetcode_py import logged_test

from .helpers import assert_find_permutation, run_find_permutation
from .solution import Solution


class TestFindPermutation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("I", [1, 2]),
            ("DI", [2, 1, 3]),
            ("D", [2, 1]),
            ("DD", [3, 2, 1]),
            ("ID", [1, 3, 2]),
            ("IID", [1, 2, 4, 3]),
            ("DDD", [4, 3, 2, 1]),
            ("IDI", [1, 3, 2, 4]),
            ("DID", [2, 1, 4, 3]),
            ("DDIIDI", [3, 2, 1, 4, 6, 5, 7]),
            ("IDIDID", [1, 3, 2, 5, 4, 7, 6]),
            ("DDDD", [5, 4, 3, 2, 1]),
        ],
    )
    def test_find_permutation(self, s: str, expected: list[int]):
        result = run_find_permutation(Solution, s)
        assert_find_permutation(result, expected)
