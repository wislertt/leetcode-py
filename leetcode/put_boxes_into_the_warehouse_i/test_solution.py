import pytest

from leetcode_py import logged_test

from .helpers import assert_max_boxes_in_warehouse, run_max_boxes_in_warehouse
from .solution import Solution


class TestPutBoxesIntoTheWarehouseI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "boxes, warehouse, expected",
        [
            ([4, 3, 4, 1], [5, 3, 3, 4, 1], 3),
            ([1, 2, 2, 3, 4], [3, 4, 1, 2], 3),
            ([1, 2, 3], [1, 2, 3, 4], 1),
            ([1], [1], 1),
            ([2], [1], 0),
            ([1, 2], [2], 1),
            ([3, 1, 2], [2, 2, 2], 2),
            ([4, 4, 4], [5], 1),
            ([1, 1, 1, 1], [2, 1, 2, 1], 4),
            ([5, 3, 2], [4, 5, 1, 3], 2),
            ([2, 2, 5, 1], [3, 1, 4], 2),
            ([1000000000], [1000000000], 1),
            ([1000000000, 1], [999999999, 1], 1),
            ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7], 1),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5),
            ([5], [2], 0),
            ([1, 2], [5, 4], 2),
            ([6, 5], [4, 5, 3, 4, 3, 2], 0),
            ([4, 6], [3, 4, 4, 2, 4], 0),
            ([6, 1, 6, 2, 2], [5, 1, 1, 3, 2], 2),
            ([5, 4, 5, 4, 4], [4, 3, 1], 1),
            ([2, 6, 1], [4, 3, 6, 1, 2], 2),
        ],
    )
    def test_max_boxes_in_warehouse(self, boxes: list[int], warehouse: list[int], expected: int):
        result = run_max_boxes_in_warehouse(Solution, boxes, warehouse)
        assert_max_boxes_in_warehouse(result, expected)
