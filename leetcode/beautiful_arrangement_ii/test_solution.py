import pytest

from leetcode_py import logged_test

from .helpers import assert_construct_array, run_construct_array
from .solution import Solution


class TestBeautifulArrangementII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k",
        [
            (3, 1),
            (3, 2),
            (2, 1),
            (4, 1),
            (4, 2),
            (4, 3),
            (5, 1),
            (5, 2),
            (5, 4),
            (6, 3),
            (7, 2),
            (7, 6),
            (8, 5),
            (10, 1),
            (10, 9),
            (100, 50),
            (1000, 999),
            (10000, 1),
            (10000, 9999),
        ],
    )
    def test_construct_array(self, n: int, k: int):
        result = run_construct_array(Solution, n, k)
        assert_construct_array(result, k)
