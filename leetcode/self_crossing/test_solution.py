import pytest

from leetcode_py import logged_test

from .helpers import assert_is_self_crossing, run_is_self_crossing
from .solution import Solution


class TestSelfCrossing:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "distance, expected",
        [
            ([2, 1, 1, 2], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 2, 1], True),
            ([1], False),
            ([1, 1], False),
            ([1, 1, 1], False),
            ([1, 1, 2, 1, 1], True),
            ([1, 2, 2, 2, 1], True),
            ([1, 1, 2, 2, 1, 1], True),
            ([1, 4, 3, 2, 1, 2], True),
            ([1, 1, 1, 1], True),
            ([2, 2, 2, 2], True),
            ([3, 3, 4, 2, 2], False),
            ([1, 2, 3, 2, 1], False),
            ([1, 1, 3, 1, 1], False),
            ([2, 1, 2, 1], True),
            ([1, 4, 5, 4, 1, 6, 6], True),
            ([2, 4, 4, 6, 4], False),
            ([4, 3, 5, 1, 5, 2, 3, 2, 4, 4], True),
            ([4, 5, 3, 2, 1, 1, 4], True),
            ([3, 3, 6, 6, 3, 6], True),
            ([1, 3, 6, 3, 4, 6, 5], True),
            ([6, 4, 6, 2, 5, 5, 6, 4, 2], True),
            ([5, 2, 5, 6, 2, 3, 5, 6, 4, 1], True),
        ],
    )
    def test_is_self_crossing(self, distance: list[int], expected: bool):
        result = run_is_self_crossing(Solution, distance)
        assert_is_self_crossing(result, expected)
