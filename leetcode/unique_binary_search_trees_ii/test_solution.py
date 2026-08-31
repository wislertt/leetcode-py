import pytest

from leetcode_py import logged_test

from .helpers import assert_generate_trees, run_generate_trees
from .solution import Solution


class TestUniqueBinarySearchTreesII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected_tree",
        [
            (1, [1]),
            (2, [1, None, 2]),
            (2, [2, 1]),
            (3, [1, None, 2, None, 3]),
            (3, [1, None, 3, 2]),
            (3, [2, 1, 3]),
            (3, [3, 1, None, None, 2]),
            (3, [3, 2, None, 1]),
            (4, [1, None, 2, None, 3, None, 4]),
            (4, [1, None, 2, None, 4, 3]),
            (4, [1, None, 3, 2, 4]),
            (4, [1, None, 4, 2, None, None, 3]),
            (4, [1, None, 4, 3, None, 2]),
            (4, [2, 1, 3, None, None, None, 4]),
            (4, [2, 1, 4, None, None, 3]),
            (4, [3, 1, 4, None, 2]),
            (4, [3, 2, 4, 1]),
            (4, [4, 1, None, None, 2, None, 3]),
            (4, [4, 1, None, None, 3, 2]),
            (4, [4, 2, None, 1, 3]),
            (4, [4, 3, None, 1, None, None, 2]),
            (4, [4, 3, None, 2, None, 1]),
            (5, [1, None, 2, None, 3, None, 4, None, 5]),
            (5, [3, 1, 4, None, 2, None, 5]),
        ],
    )
    def test_generate_trees(self, n: int, expected_tree: list[int | None]):
        result = run_generate_trees(Solution, n)
        assert_generate_trees(result, n, expected_tree)
