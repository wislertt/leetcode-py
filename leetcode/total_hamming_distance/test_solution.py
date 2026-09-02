import pytest

from leetcode_py import logged_test

from .helpers import assert_total_hamming_distance, run_total_hamming_distance
from .solution import Solution


class TestTotalHammingDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 14, 2], 6),
            ([4, 14, 4], 4),
            ([0], 0),
            ([1], 0),
            ([0, 0], 0),
            ([0, 1], 1),
            ([1, 1], 0),
            ([1, 2], 2),
            ([7, 7, 7], 0),
            ([1, 0, 1, 0], 4),
            ([3, 5, 6, 7], 9),
            ([1000000000, 999999999], 10),
            ([2, 14, 4, 2, 16], 20),
            ([6, 0, 4, 2, 8, 9], 29),
            ([9, 10, 2, 0, 10], 16),
            ([7, 6, 5], 4),
            ([4, 3], 3),
            ([101600362, 434090345, 727006828, 135258606, 920229393, 163151145], 229),
        ],
    )
    def test_total_hamming_distance(self, nums: list[int], expected: int):
        result = run_total_hamming_distance(Solution, nums)
        assert_total_hamming_distance(result, expected)
