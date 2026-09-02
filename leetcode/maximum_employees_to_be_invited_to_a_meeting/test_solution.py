import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_invitations, run_maximum_invitations
from .solution import Solution


class TestMaximumEmployeesToBeInvitedToAMeeting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "favorite, expected",
        [
            ([2, 2, 1, 2], 3),
            ([1, 2, 0], 3),
            ([3, 0, 1, 4, 1], 4),
            ([1, 0], 2),
            ([1, 2, 3, 1], 3),
            ([1, 2, 3, 0], 4),
            ([1, 0, 3, 2, 5, 4], 6),
            ([1, 0, 3, 2], 4),
            ([5, 0, 1, 2, 3, 4], 6),
            ([1, 2, 0, 4, 5, 3], 3),
            ([1, 2, 0, 4, 3], 3),
            ([3, 0, 1, 2, 5, 4, 0], 4),
            ([3, 3, 3, 1], 3),
            ([3, 9, 9, 9, 1, 8, 3, 3, 5, 1], 7),
            ([2, 2, 5, 1, 8, 8, 7, 1, 4], 7),
            ([1, 5, 5, 2, 2, 6, 4, 1, 4, 6], 4),
            ([4, 2, 5, 0, 5, 4, 4, 4], 6),
            ([4, 5, 3, 1, 1, 3], 3),
            ([2, 0, 1, 2], 3),
            ([4, 0, 0, 2, 2], 3),
        ],
    )
    def test_maximum_invitations(self, favorite: list[int], expected: int):
        result = run_maximum_invitations(Solution, favorite)
        assert_maximum_invitations(result, expected)
