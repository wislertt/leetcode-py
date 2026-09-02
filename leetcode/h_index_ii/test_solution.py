import pytest

from leetcode_py import logged_test

from .helpers import assert_h_index, run_h_index
from .solution import Solution


class TestHIndexII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "citations, expected",
        [
            ([0, 1, 3, 5, 6], 3),
            ([1, 2, 100], 2),
            ([0], 0),
            ([100], 1),
            ([0, 0], 0),
            ([1, 1], 1),
            ([0, 0, 0, 0], 0),
            ([1, 2, 3, 4, 5], 3),
            ([11, 15], 2),
            ([4, 4, 4, 4, 4], 4),
            ([0, 1, 2, 5, 6], 2),
            ([1, 1, 1, 1, 1, 1], 1),
            ([2, 2, 2], 2),
            ([0, 1, 3, 5, 6, 8, 10], 4),
            ([0, 1000, 1000, 1000, 1000], 4),
            ([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], 11),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1),
            ([0, 0, 0, 0, 0, 0, 1, 2, 3], 2),
            ([3, 3, 3], 3),
            ([0, 0, 1, 1, 2, 2], 2),
        ],
    )
    def test_h_index(self, citations: list[int], expected: int):
        result = run_h_index(Solution, citations)
        assert_h_index(result, expected)
