import pytest

from leetcode_py import logged_test

from .helpers import assert_num_rescue_boats, run_num_rescue_boats
from .solution import Solution


class TestBoatsToSavePeople:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "people, limit, expected",
        [
            ([1, 2], 3, 1),
            ([3, 2, 2, 1], 3, 3),
            ([3, 5, 3, 4], 5, 4),
            ([1, 1, 1, 1], 2, 2),
            ([5, 5, 5, 5], 5, 4),
            ([1], 1, 1),
            ([2, 2], 2, 2),
            ([1, 2, 3, 4, 5], 5, 3),
            ([3, 1, 7, 5, 2], 7, 3),
            ([1, 1, 1, 1, 1, 1], 3, 3),
            ([10], 10, 1),
            ([1, 2, 3], 3, 2),
            ([4, 4, 4, 4, 4], 8, 3),
            ([2, 1, 3, 4], 4, 3),
            ([5, 1, 4, 2], 6, 2),
            ([1, 3, 1, 3, 1, 3], 4, 3),
            ([7, 7, 7, 7], 7, 4),
            ([1, 5, 1, 5, 1], 6, 3),
        ],
    )
    def test_num_rescue_boats(self, people: list[int], limit: int, expected: int):
        result = run_num_rescue_boats(Solution, people, limit)
        assert_num_rescue_boats(result, expected)
