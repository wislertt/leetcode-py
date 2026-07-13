import pytest

from leetcode_py import logged_test

from .helpers import assert_search, run_search
from .solution import Solution


class TestTestSearchInRotatedSortedArrayII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, nums, target, expected",
        [
            (Solution, [2, 5, 6, 0, 0, 1, 2], 0, True),
            (Solution, [2, 5, 6, 0, 0, 1, 2], 3, False),
            (Solution, [1], 0, False),
            (Solution, [1], 1, True),
            (Solution, [1], 2, False),
            (Solution, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2, True),
            (Solution, [1, 1, 1, 1, 1], 2, False),
            (Solution, [3, 1], 1, True),
            (Solution, [1, 3], 3, True),
            (Solution, [1, 3, 1, 1, 1], 3, True),
            (Solution, [2, 2, 2, 3, 2, 2, 2], 3, True),
            (Solution, [4, 5, 6, 6, 7, 0, 1, 2, 4, 4], 6, True),
            (Solution, [4, 5, 6, 6, 7, 0, 1, 2, 4, 4], 8, False),
            (
                Solution,
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                13,
                True,
            ),
            (Solution, [2, 5, 6, 0, 0, 1, 2], 6, True),
            (Solution, [2, 5, 6, 0, 0, 1, 2], 2, True),
            (Solution, [1, 0, 1, 1, 1], 0, True),
            (Solution, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, False),
        ],
    )
    def test_search(self, solution_class, nums: list[int], target: int, expected: bool):
        result = run_search(solution_class, nums, target)
        assert_search(result, expected)
