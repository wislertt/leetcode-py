import pytest

from leetcode_py import logged_test

from .helpers import assert_find_tilt, run_find_tilt
from .solution import Solution


class TestBinaryTreeTilt:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3], 1),
            ([4, 2, 9, 3, 5, None, 7], 15),
            ([21, 7, 14, 1, 1, 2, 2, 3, 3], 9),
            ([], 0),
            ([0], 0),
            ([1], 0),
            ([1, 2], 2),
            ([1, None, 2], 2),
            ([-1, -2, -3], 1),
            ([1, 2, 3, 4, 5], 9),
            ([1000, -1000, 1000, -1000], 4000),
            ([327, 936, -238, -70, 707, 266], 2588),
            ([-429, -613, 170, -27, 133, -63, 679], 2195),
            ([-971, 939], 939),
            ([861, 637], 637),
            ([102], 0),
        ],
    )
    def test_find_tilt(self, root_list: list[int | None], expected: int):
        result = run_find_tilt(Solution, root_list)
        assert_find_tilt(result, expected)
