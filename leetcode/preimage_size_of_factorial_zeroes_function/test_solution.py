import pytest

from leetcode_py import logged_test

from .helpers import assert_preimage_size_fzf, run_preimage_size_fzf
from .solution import Solution


class TestPreimageSizeOfFactorialZeroesFunction:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "k, expected",
        [
            (0, 5),
            (1, 5),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 0),
            (6, 5),
            (7, 5),
            (9, 5),
            (10, 5),
            (11, 0),
            (12, 5),
            (13, 5),
            (15, 5),
            (16, 5),
            (17, 0),
            (19, 5),
            (20, 5),
            (23, 0),
            (24, 5),
            (25, 5),
            (29, 0),
            (30, 0),
            (41, 5),
            (100, 5),
            (1000000, 5),
            (999999995, 0),
            (1000000000, 5),
        ],
    )
    def test_preimage_size_fzf(self, k: int, expected: int):
        result = run_preimage_size_fzf(Solution, k)
        assert_preimage_size_fzf(result, expected)
