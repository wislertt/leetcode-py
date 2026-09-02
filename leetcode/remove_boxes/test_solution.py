import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_boxes, run_remove_boxes
from .solution import Solution


class TestRemoveBoxes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "boxes, expected",
        [
            ([1, 3, 2, 2, 2, 3, 4, 3, 1], 23),
            ([1, 1, 1], 9),
            ([1], 1),
            ([2, 2, 2, 2], 16),
            ([1, 2], 2),
            ([1, 1, 2, 2, 1, 1], 20),
            ([1, 2, 2, 2, 1], 13),
            ([3, 3, 3, 1, 2, 2, 2, 3], 26),
            ([1, 2, 3, 1, 2, 3], 8),
            ([5], 1),
            ([1, 2, 1, 2], 6),
            ([4, 4, 1, 1, 4, 4], 20),
            ([1, 3, 1, 3, 1], 11),
            ([2, 1, 2, 1, 2, 2, 1], 19),
            ([1, 1, 9, 9, 9, 1, 8, 8], 22),
            ([2, 2], 4),
            ([2, 2, 3], 5),
            ([1, 2, 1, 1, 2, 1, 1, 2, 1], 39),
            ([2, 2, 2, 1, 3, 2, 3, 3, 2, 1, 1, 3], 36),
            ([2, 1], 2),
            ([1, 1, 1, 2, 1], 17),
            ([1, 1, 2, 2, 1], 13),
            ([1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 2], 72),
            ([3, 2, 1, 3, 3, 2], 12),
            ([1, 1, 1, 1, 1], 25),
            ([1, 1, 1, 1, 1, 1, 1, 1], 64),
        ],
    )
    def test_remove_boxes(self, boxes: list[int], expected: int):
        result = run_remove_boxes(Solution, boxes)
        assert_remove_boxes(result, expected)
