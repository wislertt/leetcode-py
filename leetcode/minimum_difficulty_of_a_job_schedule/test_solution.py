import pytest

from leetcode_py import logged_test

from .helpers import assert_min_difficulty, run_min_difficulty
from .solution import Solution


class TestMinimumDifficultyOfAJobSchedule:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "job_difficulty, d, expected",
        [
            [[6, 5, 4, 3, 2, 1], 2, 7],
            [[9, 9, 9], 4, -1],
            [[1, 1, 1], 3, 3],
            [[5], 1, 5],
            [[3, 2, 1], 1, 3],
            [[1, 2, 3], 2, 4],
            [[11, 111, 22, 222, 33, 333], 3, 455],
            [[380, 302, 102, 681], 1, 681],
            [[7, 1, 7, 1, 7, 1], 3, 15],
            [[0, 0], 2, 0],
            [[186, 64, 35, 650], 2, 836],
            [[1, 1000, 1, 1000, 1], 3, 1002],
            [[635, 228, 778], 10, -1],
            [[750], 9, -1],
            [[897], 3, -1],
            [[158, 386, 684, 38, 798, 894, 546], 4, 1774],
        ],
    )
    def test_min_difficulty(self, job_difficulty: list[int], d: int, expected: int):
        result = run_min_difficulty(Solution, job_difficulty, d)
        assert_min_difficulty(result, expected)
