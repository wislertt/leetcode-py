import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_obstacle_course, run_longest_obstacle_course
from .solution import Solution


class TestFindTheLongestValidObstacleCourseAtEachPosition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "obstacles, expected",
        [
            ([1, 2, 3, 2], [1, 2, 3, 3]),
            ([2, 2, 1], [1, 2, 1]),
            ([3, 1, 5, 6, 4, 2], [1, 1, 2, 3, 2, 2]),
            ([1], [1]),
            ([5, 4, 3, 2, 1], [1, 1, 1, 1, 1]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([7, 7, 7, 7], [1, 2, 3, 4]),
            ([10000000], [1]),
            ([1, 10000000], [1, 2]),
            ([2, 1, 2, 1, 2], [1, 1, 2, 2, 3]),
            ([1, 3, 2, 4, 3, 5], [1, 2, 2, 3, 3, 4]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
            ([7, 20, 6, 5, 1, 15, 4, 5, 2, 10, 12, 12], [1, 2, 1, 1, 1, 2, 2, 3, 2, 4, 5, 6]),
            ([5, 13, 20, 6, 19, 7, 6, 15, 10, 18], [1, 2, 3, 2, 3, 3, 3, 4, 4, 5]),
            ([13, 18, 14, 1, 13, 12, 6, 6, 18, 4, 13], [1, 2, 2, 1, 2, 2, 2, 3, 4, 2, 4]),
            ([6, 13, 19, 8, 10], [1, 2, 3, 2, 3]),
            ([18, 1, 4, 2, 10, 12, 5, 10, 6, 12, 5], [1, 1, 2, 2, 3, 4, 3, 4, 4, 5, 4]),
            ([15, 10], [1, 1]),
            ([14, 13, 14, 5], [1, 1, 2, 1]),
            ([1, 6, 9, 5, 19, 8, 15, 4, 12, 5], [1, 2, 3, 2, 4, 3, 4, 2, 4, 3]),
            ([11, 14, 9], [1, 2, 1]),
            ([10, 1, 19, 15, 10, 3, 11, 10, 18, 6, 10, 19], [1, 1, 2, 2, 2, 2, 3, 3, 4, 3, 4, 5]),
        ],
    )
    def test_longest_obstacle_course(self, obstacles: list[int], expected: list[int]):
        result = run_longest_obstacle_course(Solution, obstacles)
        assert_longest_obstacle_course(result, expected)
