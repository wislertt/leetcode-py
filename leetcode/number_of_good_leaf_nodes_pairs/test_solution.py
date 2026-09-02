import pytest

from leetcode_py import logged_test

from .helpers import assert_count_pairs, run_count_pairs
from .solution import Solution


class TestNumberOfGoodLeafNodesPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, distance, expected",
        [
            ([1, 2, 3, None, 4], 3, 1),
            ([1, 2, 3, 4, 5, 6, 7], 3, 2),
            ([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2], 3, 1),
            ([1], 1, 0),
            ([1], 10, 0),
            ([1, 2], 1, 0),
            ([1, 2], 2, 0),
            ([1, 2, None], 10, 0),
            ([1, None, 2, None, 3, None, 4], 10, 0),
            ([1, 2, 3, None, None, 4, 5], 3, 3),
            ([1, 2, 3, 4, None, None, 5, 6], 4, 0),
            ([1, 2, 3, 4, 5], 10, 3),
            ([5, 1, 2, 3, None, 4, None, 6], 5, 1),
            ([9, 8, 7, 6, None, None, 5, 4, 3], 6, 3),
            ([1, 2, 3], 5, 1),
            ([1, 3, 2], 1, 0),
            ([1, 2, 3, None, None, 4, 5, 6, 7], 8, 6),
            ([1, 2, 3, 4, 5, None, None, None, None, 7, 6, 8, 9], 8, 10),
        ],
    )
    def test_count_pairs(self, root_list: list[int | None], distance: int, expected: int):
        result = run_count_pairs(Solution, root_list, distance)
        assert_count_pairs(result, expected)
