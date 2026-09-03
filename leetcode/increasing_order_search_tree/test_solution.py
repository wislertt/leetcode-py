import pytest

from leetcode_py import logged_test

from .helpers import assert_increasing_bst, run_increasing_bst
from .solution import Solution


class TestIncreasingBST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([5, 1, 7], [1, None, 5, None, 7]),
            ([1], [1]),
            ([0], [0]),
            ([1000], [1000]),
            ([2, 1], [1, None, 2]),
            ([1, None, 2], [1, None, 2]),
            ([3, 2, 4, 1], [1, None, 2, None, 3, None, 4]),
            ([4, 2, 5, 1, 3], [1, None, 2, None, 3, None, 4, None, 5]),
            ([5, 4, None, 3, None, 2, None, 1], [1, None, 2, None, 3, None, 4, None, 5]),
            ([1, None, 2, None, 3], [1, None, 2, None, 3]),
            ([2, 1, 3], [1, None, 2, None, 3]),
            (
                [10, 5, 15, 2, 7, 12, 17],
                [2, None, 5, None, 7, None, 10, None, 12, None, 15, None, 17],
            ),
            ([1, None, 1000], [1, None, 1000]),
            ([3, 2, None, 1], [1, None, 2, None, 3]),
            (
                [15, 10, 20, 8, 12, 17, 25],
                [8, None, 10, None, 12, None, 15, None, 17, None, 20, None, 25],
            ),
            ([810], [810]),
            ([769], [769]),
            ([281, None, 410, None, 805], [281, None, 410, None, 805]),
            ([70, None, 133, None, 502, None, 853], [70, None, 133, None, 502, None, 853]),
            ([530, None, 654, None, 872, None, 995], [530, None, 654, None, 872, None, 995]),
        ],
    )
    def test_increasing_bst(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_increasing_bst(Solution, root_list)
        assert_increasing_bst(result, expected_list)
