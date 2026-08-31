import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_from_leaf, run_smallest_from_leaf
from .solution import Solution


class TestSmallestStringStartingFromLeaf:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([0, 1, 2, 3, 4, 3, 4], "dba"),
            ([25, 1, 3, 1, 3, 0, 2], "adz"),
            ([2, 2, 1, None, 1, 0, None, 0], "abc"),
            ([0], "a"),
            ([25], "z"),
            ([1, 0], "ab"),
            ([0, None, 0], "aa"),
            ([4, 0, 1, 1], "bae"),
            ([25, 1, None, 0, 0, 1], "abz"),
            ([2, 0], "ac"),
            ([0, 25, 0, None, 24], "aa"),
            ([19, 3, 4, 3, None, None, 4], "ddt"),
        ],
    )
    def test_smallest_from_leaf(self, root_list: list[int | None], expected: str):
        result = run_smallest_from_leaf(Solution, root_list)
        assert_smallest_from_leaf(result, expected)
