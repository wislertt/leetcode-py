import pytest

from leetcode_py import logged_test

from .helpers import assert_flip_match_voyage, run_flip_match_voyage
from .solution import Solution


class TestFlipBinaryTreeToMatchPreorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, voyage, expected",
        [
            ([1, 2], [2, 1], [-1]),
            ([1, 2, 3], [1, 3, 2], [1]),
            ([1, 2, 3], [1, 2, 3], []),
            ([1], [1], []),
            ([1, 2, None, 3], [1, 2, 3], []),
            ([1, None, 2, None, 3], [1, 2, 3], []),
            ([2, 1, 3], [2, 3, 1], [2]),
            ([1, 2, 3, 4, None, None, 5], [1, 3, 5, 2, 4], [1]),
            ([4, 2, 1, 3], [4, 1, 2, 3], [4]),
            ([2, 5, 4, 1, None, 3], [2, 5, 1, 4, 3], []),
            ([2, 5, None, 1, 4, 3, 6], [2, 5, 4, 1, 3, 6], [5]),
            ([6, None, 2, None, 7, 3, 1, None, 5, 4], [6, 2, 7, 3, 5, 1, 4], []),
            ([6, 2, 5, 4, 7, 1, 8, 3], [6, 2, 4, 3, 7, 5, 1, 8], []),
            ([4, 5, 1, None, 2, 3], [4, 1, 3, 5, 2], [4]),
            ([6, None, 3, 2, 5, None, 4, 1], [6, 3, 5, 1, 2, 4], [3]),
            ([4, 2, None, 7, 8, 3, 1, 5, 6], [4, 2, 7, 3, 1, 8, 5, 6], []),
            ([4, None, 3, 1, 2], [3, 2, 1, 4], [-1]),
            ([1, None, 2, None, 4, 3], [1, 3, 4, 2], [-1]),
            ([4, 1, 3, None, 2], [2, 1, 3, 4], [-1]),
            ([1, 2, 3, 4, 5], [1, 2, 4, 3, 5], [-1]),
        ],
    )
    def test_flip_match_voyage(
        self, root_list: list[int | None], voyage: list[int], expected: list[int]
    ):
        result = run_flip_match_voyage(Solution, root_list, voyage)
        assert_flip_match_voyage(result, expected)
