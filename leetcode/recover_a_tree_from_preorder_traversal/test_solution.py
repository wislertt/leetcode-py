import pytest

from leetcode_py import logged_test

from .helpers import assert_recover_from_preorder, run_recover_from_preorder
from .solution import Solution


class TestRecoverATreeFromPreorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "traversal, expected_list",
        [
            ("1-2--3--4-5--6--7", [1, 2, 5, 3, 4, 6, 7]),
            ("1-2--3---4-5--6---7", [1, 2, 5, 3, None, 6, None, 4, None, 7]),
            ("1-401--349---90--88", [1, 401, None, 349, 88, 90]),
            ("1", [1]),
            ("10", [10]),
            ("1-2", [1, 2]),
            ("1-2-3", [1, 2, 3]),
            ("1-2--3-4", [1, 2, 4, 3]),
            ("5-4--3---2---2--3", [5, 4, None, 3, 3, 2, 2]),
            ("100-200--300", [100, 200, None, 300]),
            ("9-8--7---6----5", [9, 8, None, 7, None, 6, None, 5]),
            ("1-2--3--4-5--6", [1, 2, 5, 3, 4, 6]),
        ],
    )
    def test_recover_from_preorder(self, traversal: str, expected_list: list[int | None]):
        result = run_recover_from_preorder(Solution, traversal)
        assert_recover_from_preorder(result, expected_list)
