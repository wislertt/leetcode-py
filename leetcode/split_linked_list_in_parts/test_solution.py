import pytest

from leetcode_py import logged_test

from .helpers import assert_split_list_to_parts, run_split_list_to_parts
from .solution import Solution


class TestSplitLinkedListInParts:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, k, expected",
        [
            ([1, 2, 3], 5, [[1], [2], [3], [], []]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]),
            ([], 3, [[], [], []]),
            ([], 1, [[]]),
            ([1], 1, [[1]]),
            ([1], 2, [[1], []]),
            ([1], 5, [[1], [], [], [], []]),
            ([1, 2], 1, [[1, 2]]),
            ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
            ([1, 2, 3, 4, 5], 2, [[1, 2, 3], [4, 5]]),
            ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 4, [[0, 0, 0], [0, 0, 0], [0, 0], [0, 0]]),
            ([1, 2, 3], 3, [[1], [2], [3]]),
            ([5, 5, 5, 5, 5, 5, 5], 5, [[5, 5], [5, 5], [5], [5], [5]]),
            ([1, 2, 3, 4, 5, 6, 7], 7, [[1], [2], [3], [4], [5], [6], [7]]),
            ([1, 2, 3, 4, 5, 6, 7, 8], 5, [[1, 2], [3, 4], [5, 6], [7], [8]]),
        ],
    )
    def test_split_list_to_parts(self, head_vals: list[int], k: int, expected: list[list[int]]):
        result = run_split_list_to_parts(Solution, head_vals, k)
        assert_split_list_to_parts(result, expected)
