import pytest

from leetcode_py import logged_test

from .helpers import assert_count_unival_subtrees, run_count_unival_subtrees
from .solution import Solution


class TestCountUnivalueSubtrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([5, 1, 5, 5, 5, None, 5], 4),
            ([], 0),
            ([5, 5, 5, 5, 5, None, 5], 6),
            ([1], 1),
            ([1, 2, 3], 2),
            ([1, 1, 1], 3),
            ([1, 2, 2], 2),
            ([1, 1, 1, 1, 1], 5),
            ([5, 1, 5, 5, None, None, 5], 3),
            ([1, None, 1, None, 1], 3),
            ([1, 2, 1, 2, 2], 4),
            ([-1, -1, -1], 3),
            ([0, 0, 0, 1, 0], 3),
            ([7], 1),
            ([1, 2, 3, 4, 5], 3),
        ],
    )
    def test_count_unival_subtrees(self, root_list: list[int | None], expected: int):
        result = run_count_unival_subtrees(Solution, root_list)
        assert_count_unival_subtrees(result, expected)
