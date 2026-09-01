import pytest

from leetcode_py import logged_test

from .helpers import assert_assign_tasks, run_assign_tasks
from .solution import Solution


class TestProcessTasksUsingServers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "servers, tasks, expected",
        [
            ([3, 3, 2], [1, 2, 3, 2, 1, 2], [2, 2, 0, 2, 1, 2]),
            ([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1], [1, 4, 1, 4, 1, 3, 2]),
            ([7], [3], [0]),
            ([1], [2, 3, 4], [0, 0, 0]),
            ([1, 2, 3], [1], [0]),
            ([2, 2, 2], [1, 1, 1, 1], [0, 0, 0, 0]),
            ([1, 1], [5, 5, 5], [0, 1, 0]),
            ([100000, 1], [1, 100000], [1, 1]),
            ([3], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            ([4, 4], [2, 2, 2], [0, 1, 0]),
            ([2, 1, 3], [4, 1, 2, 1], [1, 0, 0, 2]),
            ([8, 1], [7, 2, 9, 1, 3, 3, 4, 6], [1, 0, 0, 1, 1, 1, 0, 1]),
            ([8, 6, 8, 2, 7], [1, 8, 1, 5, 2, 6, 1, 4], [3, 3, 1, 1, 4, 0, 4, 4]),
            ([9, 5, 6, 1], [5, 9, 8, 2, 9, 9], [3, 1, 2, 0, 3, 0]),
            ([4, 8, 7, 4, 9, 1], [2, 5, 3, 2, 1, 2, 1, 9], [5, 0, 5, 3, 2, 5, 0, 5]),
            ([5, 8, 8], [7, 1, 9, 8, 3, 5, 5, 5, 9, 8], [0, 1, 1, 2, 0, 0, 1, 2, 0, 1]),
            ([2, 6, 5, 9, 1, 2, 2, 6], [9, 8, 9, 5, 9, 6, 1, 3], [4, 0, 5, 6, 2, 1, 7, 7]),
        ],
    )
    def test_assign_tasks(self, servers: list[int], tasks: list[int], expected: list[int]):
        result = run_assign_tasks(Solution, servers, tasks)
        assert_assign_tasks(result, expected)
