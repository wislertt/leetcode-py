import pytest

from leetcode_py import logged_test

from .helpers import assert_detect_cycle, run_detect_cycle
from .solution import Solution


class TestLinkedListCycleII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, pos, expected",
        [
            ([3, 2, 0, -4], 1, 1),
            ([1, 2], 0, 0),
            ([1], -1, -1),
            ([], -1, -1),
            ([1, 2, 3, 4], -1, -1),
            ([1, 2, 3, 4], 3, 3),
            ([1, 2, 3, 4, 5], 2, 2),
            ([1, 2], 1, 1),
            ([1, 2, 3], 0, 0),
            ([1, 2, 3, 4, 5, 6], 5, 5),
            ([1, 2, 3, 4, 5], 0, 0),
            ([1, 2, 3], 2, 2),
            ([1, 2, 3, 4], 1, 1),
            ([1], 0, 0),
            ([1, 2, 3, 4, 5, 6, 7], 3, 3),
        ],
    )
    def test_detect_cycle(self, head_vals: list[int], pos: int, expected: int):
        result = run_detect_cycle(Solution, head_vals, pos)
        assert_detect_cycle(result, expected)
