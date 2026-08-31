import pytest

from leetcode_py import logged_test

from .helpers import assert_next_greater_element, run_next_greater_element
from .solution import Solution


class TestNextGreaterElementI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
            ([2, 4], [1, 2, 3, 4], [3, -1]),
            ([1], [1], [-1]),
            ([1], [1, 2], [2]),
            ([2], [1, 2], [-1]),
            ([5], [1, 5, 3], [-1]),
            ([1, 5], [5, 1, 3], [3, -1]),
            ([3, 5], [1, 3, 5, 7], [5, 7]),
            ([7, 3, 1], [1, 3, 5, 7], [-1, 5, 3]),
            ([0], [0, 10000], [10000]),
            ([4, 2], [1, 2, 3, 4], [-1, 3]),
            ([2, 3], [3, 2, 1, 4], [4, 4]),
            ([10000], [0, 9999, 10000], [-1]),
        ],
    )
    def test_next_greater_element(self, nums1: list[int], nums2: list[int], expected: list[int]):
        result = run_next_greater_element(Solution, nums1, nums2)
        assert_next_greater_element(result, expected)
