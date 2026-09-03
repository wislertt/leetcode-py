import pytest

from leetcode_py import logged_test

from .helpers import assert_min_camera_cover, run_min_camera_cover
from .solution import Solution


class TestBinaryTreeCameras:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([0], 1),
            ([0, 0], 1),
            ([0, 0, 0], 1),
            ([0, 0, None, 0, 0], 1),
            ([0, 0, None, 0, None, 0, None, None, 0], 2),
            ([0, None, 0, None, 0, None, 0], 2),
            ([0, 0, 0, None, None, None, 0], 2),
            ([0, 0, None, 0, None, 0], 2),
            ([0, 0, None, None, 0], 1),
            ([0, 0, 0, 0], 2),
            ([0, 0, 0, None, 0], 2),
            ([0, None, 0, None, 0], 1),
            ([0, 0, 0, None, 0, 0, 0, 0, None, None, None, 0], 3),
            ([0, 0, 0, None, 0, None, None, 0, 0, None, 0], 3),
            ([0, None, 0, 0, 0, None, None, None, 0], 2),
            ([0, 0, 0, 0, 0, 0, None, None, None, 0, 0], 3),
            ([0, 0, 0, None, 0, None, None, None, 0], 2),
            ([0, 0, 0, None, 0, 0, None, 0], 2),
            ([0, 0, 0, None, None, 0, 0, 0, None, None, 0, 0, 0], 3),
            ([0, 0, 0, 0, None, None, 0, None, None, 0, 0, 0, None, None, 0], 4),
        ],
    )
    def test_min_camera_cover(self, root_list: list[int | None], expected: int):
        result = run_min_camera_cover(Solution, root_list)
        assert_min_camera_cover(result, expected)
