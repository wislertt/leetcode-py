import pytest

from leetcode_py import logged_test

from .helpers import assert_mirror_reflection, run_mirror_reflection
from .solution import Solution


class TestMirrorReflection:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "p, q, expected",
        [
            (2, 1, 2),
            (3, 1, 1),
            (1, 1, 1),
            (2, 2, 1),
            (4, 2, 2),
            (5, 2, 0),
            (6, 3, 2),
            (7, 3, 1),
            (8, 6, 2),
            (9, 6, 0),
            (10, 4, 0),
            (12, 8, 0),
            (15, 10, 0),
            (21, 14, 0),
            (11, 7, 1),
            (13, 5, 1),
            (16, 12, 2),
            (100, 99, 2),
            (999, 999, 1),
            (1000, 1, 2),
            (1000, 999, 2),
        ],
    )
    def test_mirror_reflection(self, p: int, q: int, expected: int):
        result = run_mirror_reflection(Solution, p, q)
        assert_mirror_reflection(result, expected)
