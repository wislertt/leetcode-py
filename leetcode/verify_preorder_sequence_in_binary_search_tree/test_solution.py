import pytest

from leetcode_py import logged_test

from .helpers import assert_verify_preorder, run_verify_preorder
from .solution import Solution


class TestVerifyPreorderSequenceInBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "preorder, expected",
        [
            ([5, 2, 1, 3, 6], True),
            ([5, 2, 6, 1, 3], False),
            ([1], True),
            ([2, 1], True),
            ([1, 2], True),
            ([2, 1, 3], True),
            ([3, 2, 1], True),
            ([1, 3, 2], True),
            ([2, 3, 1], False),
            ([1, 2, 3], True),
            ([3, 2, 4, 1, 5], False),
            ([3, 4, 2, 5, 1], False),
            ([8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15], True),
            ([8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 15, 13], False),
            ([10, 5, 3, 1, 4, 7, 6, 8, 15, 12, 11, 13, 20, 18, 25], True),
            ([10, 5, 3, 4, 1, 7, 6, 8, 15, 12, 11, 13, 20, 18, 25], False),
            ([2, 1, 3, 4, 5, 6, 7], True),
            ([7, 6, 5, 4, 3, 2, 1], True),
            ([4, 2, 1, 3, 6, 5, 7], True),
            ([4, 6, 5, 7, 2, 1, 3], False),
        ],
    )
    def test_verify_preorder(self, preorder: list[int], expected: bool):
        result = run_verify_preorder(Solution, preorder)
        assert_verify_preorder(result, expected)
