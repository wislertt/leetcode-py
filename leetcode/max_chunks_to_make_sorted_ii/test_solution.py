import pytest

from leetcode_py import logged_test

from .helpers import assert_max_chunks_to_sorted, run_max_chunks_to_sorted
from .solution import Solution


class TestMaxChunksToMakeSortedII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([5, 4, 3, 2, 1], 1),
            ([2, 1, 3, 4, 4], 4),
            ([0], 1),
            ([1], 1),
            ([0, 0], 2),
            ([1, 0, 1], 2),
            ([4, 4, 4, 4], 4),
            ([1, 2, 0, 3], 2),
            ([0, 2, 1, 3], 3),
            ([2, 1, 3, 4, 4], 4),
            ([1, 0, 2, 3, 4], 4),
            ([3, 0, 2, 1], 1),
            ([0, 1, 2], 3),
            ([2, 0, 1], 1),
            ([5, 5, 1, 2, 2], 1),
            ([1, 1, 0, 0, 3, 3], 3),
            ([0, 1, 0, 1, 0], 2),
            ([2, 1, 1, 2, 2], 3),
            ([4, 3, 6, 5, 7, 7, 8], 5),
            ([1, 0, 1, 0, 2], 2),
            ([4, 7], 2),
            ([3, 7, 2, 8, 0], 1),
            ([0, 4, 1, 3], 2),
            ([0, 5, 8, 4, 8], 3),
        ],
    )
    def test_max_chunks_to_sorted(self, arr: list[int], expected: int):
        result = run_max_chunks_to_sorted(Solution, arr)
        assert_max_chunks_to_sorted(result, expected)
