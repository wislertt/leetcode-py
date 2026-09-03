import pytest

from leetcode_py import logged_test

from .helpers import assert_num_friend_requests, run_num_friend_requests
from .solution import Solution


class TestFriendsOfAppropriateAges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ages, expected",
        [
            ([16, 16], 2),
            ([16, 17, 18], 2),
            ([20, 30, 100, 110, 120], 3),
            ([1], 0),
            ([120], 0),
            ([14, 14], 0),
            ([15, 15], 2),
            ([15, 16], 0),
            ([57, 69], 1),
            ([100, 99, 101], 3),
            ([30, 101, 25, 101], 3),
            ([1, 2], 0),
            ([108, 115, 55], 1),
            ([68, 68, 20, 35], 2),
            ([55, 56, 57, 58], 6),
            ([83, 95, 38, 74, 103, 115], 10),
            ([82, 112, 95], 3),
            ([77, 25, 103, 5, 15], 1),
            ([76, 48, 100, 34, 87, 37, 37], 11),
            ([2, 29, 34, 64, 68, 110], 4),
        ],
    )
    def test_num_friend_requests(self, ages: list[int], expected: int):
        result = run_num_friend_requests(Solution, ages)
        assert_num_friend_requests(result, expected)
