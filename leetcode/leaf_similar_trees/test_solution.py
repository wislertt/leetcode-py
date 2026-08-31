import pytest

from leetcode_py import logged_test

from .helpers import assert_leaf_similar, run_leaf_similar
from .solution import Solution


class TestLeafSimilarTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root1_list, root2_list, expected",
        [
            (
                [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
                [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
                True,
            ),
            ([1, 2, 3], [1, 3, 2], False),
            ([1], [1], True),
            ([1], [2], False),
            ([1, 2], [1, 2], True),
            ([1, 2], [2, 1], False),
            (
                [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
                [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
                True,
            ),
            ([2, 2, 2, None, 2], [2, 2, 2], True),
            ([0, 200, 100], [0, 100, 200], False),
            ([1, 2, 3, None, 4], [3, None, 4, 2, None, None, 1], False),
            ([5, 4, 3, 2], [5, 4, 2, 3], False),
            ([7, 8], [7], False),
            ([1, None, 2, None, 3], [1, None, 2, None, 3], True),
            ([1, 2, None, 3], [1, None, 2, None, 3], True),
        ],
    )
    def test_leaf_similar(
        self, root1_list: list[int | None], root2_list: list[int | None], expected: bool
    ):
        result = run_leaf_similar(Solution, root1_list, root2_list)
        assert_leaf_similar(result, expected)
