import pytest

from leetcode_py import logged_test

from .helpers import assert_num_trees, run_num_trees
from .solution import Solution


class TestUniqueBinarySearchTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 5),
            (4, 14),
            (5, 42),
            (6, 132),
            (7, 429),
            (8, 1430),
            (9, 4862),
            (10, 16796),
            (11, 58786),
            (12, 208012),
            (13, 742900),
            (14, 2674440),
            (15, 9694845),
            (16, 35357670),
            (17, 129644790),
            (18, 477638700),
            (19, 1767263190),
        ],
    )
    def test_num_trees(self, n: int, expected: int):
        result = run_num_trees(Solution, n)
        assert_num_trees(result, expected)
