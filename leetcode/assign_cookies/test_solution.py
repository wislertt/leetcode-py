import pytest

from leetcode_py import logged_test

from .helpers import assert_find_content_children, run_find_content_children
from .solution import Solution


class TestAssignCookies:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "g, s, expected",
        [
            ([1, 2, 3], [1, 1], 1),
            ([1, 2], [1, 2, 3], 2),
            ([1, 2, 3], [], 0),
            ([1], [], 0),
            ([5], [5], 1),
            ([5], [4], 0),
            ([1, 2, 7], [1, 3, 5, 9], 3),
            ([10, 9, 8, 7], [5, 6, 7, 8, 9, 10], 4),
            ([1, 2, 3], [3], 1),
            ([2, 2, 2], [2, 2], 2),
            ([1, 5, 9], [1, 5, 9], 3),
            ([3, 7, 9], [4, 8], 2),
            ([4, 5, 6], [1, 2, 3], 0),
            ([7, 8, 9, 10], [1, 2, 3, 4, 5], 0),
            ([1, 1, 1], [1, 1, 1], 3),
        ],
    )
    def test_find_content_children(self, g: list[int], s: list[int], expected: int):
        result = run_find_content_children(Solution, g, s)
        assert_find_content_children(result, expected)
