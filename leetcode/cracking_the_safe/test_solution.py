import pytest

from leetcode_py import logged_test

from .helpers import assert_crack_safe, run_crack_safe
from .solution import Solution


class TestCrackingTheSafe:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (1, 1, (1, 1)),
            (1, 2, (1, 2)),
            (1, 3, (1, 3)),
            (2, 1, (2, 1)),
            (2, 2, (2, 2)),
            (2, 3, (2, 3)),
            (3, 1, (3, 1)),
            (3, 2, (3, 2)),
            (3, 3, (3, 3)),
            (1, 4, (1, 4)),
            (1, 10, (1, 10)),
            (2, 4, (2, 4)),
            (3, 4, (3, 4)),
            (4, 1, (4, 1)),
            (4, 2, (4, 2)),
        ],
    )
    def test_crack_safe(self, n: int, k: int, expected: tuple[int, int]):
        result = run_crack_safe(Solution, n, k)
        assert_crack_safe(result, expected)
