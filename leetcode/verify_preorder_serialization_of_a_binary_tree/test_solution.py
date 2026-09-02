import pytest

from leetcode_py import logged_test

from .helpers import assert_is_valid_serialization, run_is_valid_serialization
from .solution import Solution


class TestVerifyPreorderSerializationOfABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "preorder, expected",
        [
            ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
            ("1,#", False),
            ("9,#,#,1", False),
            ("#", True),
            ("9,#", False),
            ("#,#", False),
            ("9,#,#", True),
            ("1,#,#,#", False),
            ("0,#,#", True),
            ("1,2,#,#,3,#,#", True),
            ("1,#,2,#,#", True),
            ("1,#,2,#", False),
            ("9,3,4,#,#,#,#", True),
            ("100,50,#,#,75,#,#", True),
            ("1,1,#,#,1,#,#", True),
            ("9,#,#,1,#,#", False),
            ("41,50,9,12,#,#,#,#,4,#,#", True),
            ("80,7,50,#,#,17,#,#,#", True),
        ],
    )
    def test_is_valid_serialization(self, preorder: str, expected: bool):
        result = run_is_valid_serialization(Solution, preorder)
        assert_is_valid_serialization(result, expected)
