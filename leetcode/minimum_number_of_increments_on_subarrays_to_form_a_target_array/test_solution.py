import pytest

from leetcode_py import logged_test

from .helpers import assert_min_number_operations, run_min_number_operations
from .solution import Solution


class TestMinimumNumberOfIncrementsOnSubarraysToFormATargetArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, expected",
        [
            ([1, 2, 3, 2, 1], 3),
            ([3, 1, 1, 2], 4),
            ([3, 1, 5, 4, 2], 7),
            ([1], 1),
            ([5], 5),
            ([100000], 100000),
            ([1, 1, 1, 1], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 5),
            ([100000, 1], 100000),
            ([1, 100000], 100000),
            ([10, 1, 10, 1, 10], 28),
            ([2, 1, 3, 1, 4, 1, 5], 11),
            ([4, 4, 5, 1, 1, 6], 10),
            ([3, 3, 3, 2, 2, 2], 3),
            ([4, 1, 1, 6, 2, 8, 5, 6, 4, 5], 17),
            ([1, 4, 7, 5, 3, 6, 5, 1], 10),
            ([7, 1, 2, 3, 4, 1], 10),
            ([8, 3, 3, 6], 11),
            ([5, 3, 2, 5, 5, 4, 4, 2, 8], 14),
        ],
    )
    def test_min_number_operations(self, target: list[int], expected: int):
        result = run_min_number_operations(Solution, target)
        assert_min_number_operations(result, expected)
