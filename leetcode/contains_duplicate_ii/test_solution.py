import pytest

from leetcode_py import logged_test

from .helpers import assert_contains_nearby_duplicate, run_contains_nearby_duplicate
from .solution import Solution


class TestContainsDuplicateII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3, 1], 3, True),
            ([1, 0, 1, 1], 1, True),
            ([1, 2, 3, 1, 2, 3], 2, False),
            ([1], 1, False),
            ([1, 1], 0, False),
            ([1, 1], 1, True),
            ([1, 2, 1], 2, True),
            ([1, 2, 1], 1, False),
            ([1, 2, 3, 4, 1], 3, False),
            ([1, 2, 3, 4, 1], 4, True),
            ([5, 5, 5], 1, True),
            ([1, 2, 3, 4, 5], 3, False),
            ([1, 2, 3, 1, 1], 2, True),
            ([99, 99], 0, False),
            ([1, 2, 3, 4, 5, 1], 5, True),
        ],
    )
    def test_contains_nearby_duplicate(self, nums: list[int], k: int, expected: bool):
        result = run_contains_nearby_duplicate(Solution, nums, k)
        assert_contains_nearby_duplicate(result, expected)
