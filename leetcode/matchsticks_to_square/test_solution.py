import pytest

from leetcode_py import logged_test

from .helpers import assert_makesquare, run_makesquare
from .solution import Solution


class TestMatchsticksToSquare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matchsticks, expected",
        [
            ([1, 1, 2, 2, 2], True),
            ([3, 3, 3, 3, 4], False),
            ([1, 1, 1, 1], True),
            ([4, 4, 4, 4], True),
            ([2, 2, 2, 2, 2, 2, 2, 2], True),
            ([5], False),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),
            ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], True),
            ([1, 1, 1, 1, 1], False),
            ([2, 2, 2, 2, 4, 4, 4, 4], True),
            ([1, 1, 1, 1, 2, 2, 2, 2], True),
            ([3, 3, 3, 3, 3, 3, 3, 3], True),
            ([7, 7, 7, 7], True),
            ([7, 7, 7, 7, 7], False),
            ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2], False),
        ],
    )
    def test_makesquare(self, matchsticks: list[int], expected: bool):
        result = run_makesquare(Solution, matchsticks)
        assert_makesquare(result, expected)
