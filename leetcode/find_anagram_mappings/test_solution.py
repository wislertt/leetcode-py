import pytest

from leetcode_py import logged_test

from .helpers import assert_anagram_mappings, run_anagram_mappings
from .solution import Solution


class TestFindAnagramMappings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([12, 28, 46, 32, 50], [50, 12, 32, 46, 28], [1, 4, 3, 2, 0]),
            ([84, 46], [84, 46], [0, 1]),
            ([1], [1], [0]),
            ([1, 2, 3], [3, 2, 1], [2, 1, 0]),
            ([7, 7, 7], [7, 7, 7], [2, 2, 2]),
            ([1, 1, 2], [2, 1, 1], [2, 2, 0]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [4, 3, 2, 1, 0]),
            ([0, 105, 0], [0, 0, 105], [1, 2, 1]),
            ([9], [9], [0]),
            ([10, 20, 30, 40], [40, 30, 20, 10], [3, 2, 1, 0]),
            ([3, 1, 2, 2, 1], [1, 2, 2, 1, 3], [4, 3, 2, 2, 3]),
            ([100, 100, 50, 50], [50, 100, 100, 50], [2, 2, 3, 3]),
        ],
    )
    def test_anagram_mappings(self, nums1: list[int], nums2: list[int], expected: list[int]):
        result = run_anagram_mappings(Solution, nums1, nums2)
        assert_anagram_mappings(result, expected)
