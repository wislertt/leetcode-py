import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_partition, run_valid_partition
from .solution import Solution


class TestCheckIfThereIsValidPartitionForTheArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 4, 4, 5, 6], True),
            ([1, 1, 1, 2], False),
            ([2, 2], True),
            ([1, 2], False),
            ([1, 2, 3], True),
            ([3, 4, 5, 6], False),
            ([1, 1, 2, 2, 3, 3], True),
            ([1, 1, 1, 1, 1, 1], True),
            ([5, 6, 7, 8, 9, 10], True),
            ([1, 1, 2], False),
            ([7, 7, 8, 8, 9], False),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], True),
            ([1, 2, 3, 1], False),
            ([10, 10, 10, 10], True),
            ([1, 1, 3, 4, 5], True),
            ([2, 3, 4, 4, 4], True),
            ([713, 713, 600, 600, 600], True),
            ([10, 6, 10, 7, 10, 1, 7, 9, 4], False),
            ([749, 749, 749, 813, 813, 828, 829, 830, 433, 434, 435], True),
            ([5, 9, 8, 10, 2], False),
            ([9, 4, 4, 4, 3, 9, 6, 2], False),
            ([50, 51, 52, 560, 560, 560], True),
            ([6, 5, 6, 10], False),
            ([7, 10, 6, 8, 6, 3, 8, 7, 10], False),
            ([968, 968, 968, 736, 737, 738], True),
            ([834, 834, 834], True),
            ([996, 996, 996, 682, 682], True),
            ([116, 116, 650, 651, 652], True),
            ([6, 1, 9, 1, 6, 5, 6, 8], False),
            ([737, 737, 737], True),
            ([226, 226, 731, 731], True),
            ([692, 692], True),
        ],
    )
    def test_valid_partition(self, nums: list[int], expected: bool):
        result = run_valid_partition(Solution, nums)
        assert_valid_partition(result, expected)
