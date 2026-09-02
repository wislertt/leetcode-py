import pytest

from leetcode_py import logged_test

from .helpers import assert_h_index, run_h_index
from .solution import Solution


class TestHIndex:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "citations, expected",
        [
            ([3, 0, 6, 1, 5], 3),
            ([1, 3, 1], 1),
            ([0], 0),
            ([100], 1),
            ([0, 0], 0),
            ([1, 1, 1, 1], 1),
            ([4, 4, 4, 4], 4),
            ([0, 1, 3, 5, 6], 3),
            ([10, 8, 5, 4, 3], 4),
            ([25, 8, 5, 3, 3], 3),
            ([2, 2], 2),
            ([1, 2, 2, 3, 3, 4, 5, 6], 3),
            ([11, 15], 2),
            ([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], 10),
            ([7, 0, 6, 1, 5, 8, 9, 2], 5),
            ([5, 5, 5, 5, 5], 5),
            ([1, 0, 1, 0, 1, 0], 1),
            ([3, 3, 3], 3),
            ([2, 7, 4, 1, 8, 1], 3),
            ([6, 6, 6, 6, 6, 6], 6),
            ([7, 5, 6], 3),
            ([12], 1),
            ([0, 10, 4, 3], 3),
            ([0, 5, 6, 7], 3),
            ([0, 6, 6, 5, 8, 8], 5),
            ([12, 9, 11, 0, 12], 4),
        ],
    )
    def test_h_index(self, citations: list[int], expected: int):
        result = run_h_index(Solution, citations)
        assert_h_index(result, expected)
