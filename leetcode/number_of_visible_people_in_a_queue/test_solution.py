import pytest

from leetcode_py import logged_test

from .helpers import assert_can_see_persons_count, run_can_see_persons_count
from .solution import Solution


class TestNumberOfVisiblePeopleInAQueue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, expected",
        [
            ([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]),
            ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0]),
            ([1], [0]),
            ([2, 1], [1, 0]),
            ([1, 2], [1, 0]),
            ([1, 2, 3, 4, 5], [1, 1, 1, 1, 0]),
            ([5, 4, 3, 2, 1], [1, 1, 1, 1, 0]),
            ([3, 1, 4, 2, 5], [2, 1, 2, 1, 0]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0]),
            ([1, 4, 2, 5, 3, 6], [1, 2, 1, 2, 1, 0]),
            ([100000], [0]),
            ([4, 2, 3, 1], [2, 1, 1, 0]),
            ([6, 2, 4, 1, 5, 3], [3, 1, 2, 1, 1, 0]),
            ([29, 17, 15, 23, 9, 10], [2, 2, 1, 2, 1, 0]),
            ([7, 38, 13, 8, 6, 11, 24], [1, 2, 3, 2, 1, 1, 0]),
            ([15, 9, 21, 34, 17, 35, 6, 32, 13], [2, 1, 1, 2, 1, 2, 1, 1, 0]),
            ([25, 19, 4, 10, 36, 8], [2, 3, 1, 1, 1, 0]),
            ([26, 1, 27, 34, 25, 3, 15, 10], [2, 1, 1, 1, 2, 1, 1, 0]),
            ([14, 17, 2, 7, 18, 23, 30], [1, 3, 1, 1, 1, 1, 0]),
            ([20, 33, 25, 16, 23, 32], [1, 2, 3, 1, 1, 0]),
        ],
    )
    def test_can_see_persons_count(self, heights: list[int], expected: list[int]):
        result = run_can_see_persons_count(Solution, heights)
        assert_can_see_persons_count(result, expected)
