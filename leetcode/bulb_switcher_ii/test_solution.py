import pytest

from leetcode_py import logged_test

from .helpers import assert_flip_lights, run_flip_lights
from .solution import Solution


class TestBulbSwitcherII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, presses, expected",
        [
            (1, 1, 2),
            (2, 1, 3),
            (3, 1, 4),
            (1, 0, 1),
            (1, 2, 2),
            (2, 2, 4),
            (2, 3, 4),
            (3, 2, 7),
            (3, 3, 8),
            (4, 0, 1),
            (4, 1, 4),
            (4, 2, 7),
            (6, 3, 8),
            (7, 4, 8),
            (10, 5, 8),
            (1, 1000, 2),
            (2, 1000, 4),
            (999, 999, 8),
            (1000, 0, 1),
            (1000, 1, 4),
        ],
    )
    def test_flip_lights(self, n: int, presses: int, expected: int):
        result = run_flip_lights(Solution, n, presses)
        assert_flip_lights(result, expected)
