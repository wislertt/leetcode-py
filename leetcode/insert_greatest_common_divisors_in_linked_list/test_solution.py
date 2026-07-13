import pytest

from leetcode_py import logged_test

from .helpers import assert_insert_greatest_common_divisors, run_insert_greatest_common_divisors
from .solution import Solution


class TestInsertGreatestCommonDivisorsInLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),
            ([7], [7]),
            ([1], [1]),
            ([2, 2], [2, 2, 2]),
            ([4, 6], [4, 2, 6]),
            ([3, 5], [3, 1, 5]),
            ([12, 8], [12, 4, 8]),
            ([100, 10], [100, 10, 10]),
            ([1, 2, 3], [1, 1, 2, 1, 3]),
            ([2, 4, 8], [2, 2, 4, 4, 8]),
            ([6, 9, 12], [6, 3, 9, 3, 12]),
            ([10, 10, 10], [10, 10, 10, 10, 10]),
            ([1000, 500], [1000, 500, 500]),
            ([7, 13], [7, 1, 13]),
            ([5, 25, 125], [5, 5, 25, 25, 125]),
        ],
    )
    def test_insert_greatest_common_divisors(self, head_list: list[int], expected_list: list[int]):
        result = run_insert_greatest_common_divisors(Solution, head_list)
        assert_insert_greatest_common_divisors(result, expected_list)
