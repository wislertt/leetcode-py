import pytest

from leetcode_py import logged_test

from .helpers import assert_min_end, run_min_end
from .solution import Solution


class TestMinimumArrayEnd:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, x, expected",
        [
            (3, 4, 6),
            (2, 7, 15),
            (1, 5, 5),
            (1, 1, 1),
            (1, 100, 100),
            (2, 1, 3),
            (3, 1, 5),
            (4, 1, 7),
            (5, 2, 10),
            (2, 8, 9),
            (2, 1024, 1025),
            (10, 1, 19),
            (7, 5, 29),
            (3, 2, 6),
            (6, 4, 13),
        ],
    )
    def test_min_end(self, n: int, x: int, expected: int):
        result = run_min_end(Solution, n, x)
        assert_min_end(result, expected)
