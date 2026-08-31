import pytest

from leetcode_py import logged_test

from .helpers import assert_find_duplicate_subtrees, run_find_duplicate_subtrees
from .solution import Solution


class TestFindDuplicateSubtrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4, None, 2, 4, None, None, 4], [[2, 4], [4]]),
            ([2, 1, 1], [[1]]),
            ([2, 2, 2, 3, None, 3, None], [[2, 3], [3]]),
            ([1], []),
            ([1, 1, 1], [[1]]),
            ([0, 0, 0, 0, None, None, 0, None, None, None, 0], [[0]]),
            ([2, 2, 2, 2, 2, 2], [[2]]),
            ([1, 2, 3], []),
            ([1, 1], []),
            ([1, None, 1], []),
            ([5, 4, 4, 3, 3, None, None, 2, 2], [[2]]),
            ([1, 2, 2, 3, 3, 3, 3], [[2, 3, 3], [3]]),
        ],
    )
    def test_find_duplicate_subtrees(
        self, root_list: list[int | None], expected: list[list[int | None]]
    ):
        result = run_find_duplicate_subtrees(Solution, root_list)
        assert_find_duplicate_subtrees(result, expected)
