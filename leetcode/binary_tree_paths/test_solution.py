import pytest

from leetcode_py import logged_test

from .helpers import assert_binary_tree_paths, run_binary_tree_paths
from .solution import Solution


class TestBinaryTreePaths:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, None, 5], ["1->2->5", "1->3"]),
            ([1], ["1"]),
            ([1, 2], ["1->2"]),
            ([1, None, 2], ["1->2"]),
            ([1, 2, 3, 4, 5], ["1->2->4", "1->2->5", "1->3"]),
            ([-1, None, 5], ["-1->5"]),
            ([0], ["0"]),
            ([1, 2, 3, 4], ["1->2->4", "1->3"]),
            ([5, 3, 8, 1, None, 7, 9], ["5->3->1", "5->8->7", "5->8->9"]),
            ([1, 2, 3, None, 4], ["1->2->4", "1->3"]),
            ([-100], ["-100"]),
            ([100], ["100"]),
            ([1, 2, None, 3], ["1->2->3"]),
            ([1, 2, None, 3, None, 4], ["1->2->3->4"]),
            ([2, 1, 3, None, None, None, 4], ["2->1", "2->3->4"]),
            ([-19], ["-19"]),
            ([36, -97, -68, -99, 18, -40], ["36->-97->-99", "36->-97->18", "36->-68->-40"]),
            ([59, 100, -59, None, None, None, -80], ["59->100", "59->-59->-80"]),
        ],
    )
    def test_binary_tree_paths(self, root_list: list[int | None], expected: list[str]):
        result = run_binary_tree_paths(Solution, root_list)
        assert_binary_tree_paths(result, expected)
