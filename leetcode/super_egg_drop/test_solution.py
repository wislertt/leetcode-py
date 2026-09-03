import pytest

from leetcode_py import logged_test

from .helpers import assert_super_egg_drop, run_super_egg_drop
from .solution import Solution


class TestSuperEggDrop:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "k, n, expected",
        [
            (1, 2, 2),
            (2, 6, 3),
            (3, 14, 4),
            (1, 1, 1),
            (1, 10, 10),
            (1, 100, 100),
            (2, 1, 1),
            (2, 3, 2),
            (2, 10, 4),
            (3, 1, 1),
            (3, 6, 3),
            (4, 100, 8),
            (2, 100, 14),
            (10, 5, 3),
            (100, 10000, 14),
            (5, 1000, 11),
            (10, 1000, 10),
            (100, 1, 1),
            (7, 500, 9),
            (2, 5000, 100),
        ],
    )
    def test_super_egg_drop(self, k: int, n: int, expected: int):
        result = run_super_egg_drop(Solution, k, n)
        assert_super_egg_drop(result, expected)
