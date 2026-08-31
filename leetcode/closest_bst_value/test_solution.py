import pytest

from leetcode_py import logged_test

from .helpers import assert_closest_value, run_closest_value
from .solution import Solution


class TestClosestBinarySearchTreeValue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target, expected",
        [
            ([4, 2, 5, 1, 3], 3.714286, 4),
            ([1], 4.428571, 1),
            ([4, 2, 5, 1, 3], 3.5, 3),
            ([2, 1, 3], 2.5, 2),
            ([2, 1, 3], 1.5, 1),
            ([1, None, 2], 1.7, 2),
            ([5, 3, 10, 1, 4, 8, 12], 7, 8),
            ([5, 3, 10, 1, 4, 8, 12], 2, 1),
            ([1000000000], -1000000000, 1000000000),
            ([1, None, 3, None, None, 2], 2.6, 3),
            ([4, 2, 6, 1, 3, 5, 7], 5.0, 5),
            ([4, 2, 6, 1, 3, 5, 7], 6.4, 6),
            ([9, 4, 20, 2, 6, 17, 25], 14.0, 17),
            ([9, 4, 20, 2, 6, 17, 25], 26.5, 25),
            ([9, 4, 20, 2, 6, 17, 25], 1.0, 2),
        ],
    )
    def test_closest_value(self, root_list: list[int | None], target: float, expected: int):
        result = run_closest_value(Solution, root_list, target)
        assert_closest_value(result, expected)
