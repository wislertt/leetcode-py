import pytest

from leetcode_py import logged_test

from .helpers import assert_judge_point24, run_judge_point24
from .solution import Solution


class TestGame24:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "cards, expected",
        [
            ([4, 1, 8, 7], True),
            ([1, 2, 1, 2], False),
            ([1, 1, 1, 1], False),
            ([3, 3, 8, 8], True),
            ([1, 5, 5, 5], True),
            ([1, 3, 4, 6], True),
            ([1, 1, 2, 7], True),
            ([2, 2, 2, 2], False),
            ([1, 1, 1, 8], True),
            ([4, 6, 7, 8], True),
            ([3, 4, 5, 6], True),
            ([2, 3, 5, 7], True),
            ([1, 9, 9, 9], False),
            ([8, 8, 8, 8], False),
            ([9, 9, 9, 1], False),
            ([2, 4, 6, 8], True),
            ([5, 7, 7, 8], False),
            ([1, 2, 3, 4], True),
            ([6, 6, 6, 6], True),
            ([3, 7, 8, 9], True),
        ],
    )
    def test_judge_point24(self, cards: list[int], expected: bool):
        result = run_judge_point24(Solution, cards)
        assert_judge_point24(result, expected)
