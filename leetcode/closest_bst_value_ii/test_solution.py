import pytest

from leetcode_py import logged_test

from .helpers import assert_closest_k_values, run_closest_k_values
from .solution import Solution


class TestClosestBinarySearchTreeValueII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target, k, expected",
        [
            ([4, 2, 5, 1, 3], 3.714286, 2, [3, 4]),
            ([1], 0.0, 1, [1]),
            ([4, 2, 5, 1, 3], 3.7, 3, [3, 4, 5]),
            ([4, 2, 5, 1, 3], 2.5, 2, [2, 3]),
            ([4, 2, 5, 1, 3], 3.8, 2, [3, 4]),
            ([4, 2, 5, 1, 3], 4.0, 5, [1, 2, 3, 4, 5]),
            ([4, 2, 5, 1, 3], 1.0, 2, [1, 2]),
            ([1, None, 2], 1.4, 2, [1, 2]),
            ([1, None, 2], 1.9, 1, [2]),
            ([5, 3, 10, 1, 4, 8, 12], 7.6, 3, [5, 8, 10]),
            ([5, 3, 10, 1, 4, 8, 12], 7.0, 2, [5, 8]),
            ([4, 2, 6, 1, 3, 5, 7], 3.6, 4, [2, 3, 4, 5]),
            ([4, 2, 6, 1, 3, 5, 7], 7.5, 3, [5, 6, 7]),
            ([2, 1, 4, None, None, 3], 3.2, 2, [3, 4]),
        ],
    )
    def test_closest_k_values(
        self, root_list: list[int | None], target: float, k: int, expected: list[int]
    ):
        result = run_closest_k_values(Solution, root_list, target, k)
        assert_closest_k_values(result, expected)
