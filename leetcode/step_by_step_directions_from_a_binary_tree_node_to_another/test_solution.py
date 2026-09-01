import pytest

from leetcode_py import logged_test

from .helpers import assert_get_directions, run_get_directions
from .solution import Solution


class TestStepByStepDirectionsFromABinaryTreeNodeToAnother:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, start_value, dest_value, expected",
        [
            ([5, 1, 2, 3, None, 6, 4], 3, 6, "UURL"),
            ([2, 1], 2, 1, "L"),
            ([2, 1], 1, 2, "U"),
            ([1, 2, 3], 2, 3, "UR"),
            ([1, 2, 3], 3, 2, "UL"),
            ([1, 2, 3, 4, 5, 6, 7], 4, 7, "UURR"),
            ([1, 2, 3, 4, 5, 6, 7], 7, 4, "UULL"),
            ([1, 2, None, 3, None, 4], 4, 1, "UUU"),
            ([1, None, 2, None, 3], 1, 3, "RR"),
            ([5, 3, 8, 1, 4, 7, 9, None, None, 2, 6], 2, 6, "UR"),
            ([5, 3, 8, 1, 4, 7, 9, None, None, 2, 6], 3, 9, "URR"),
            ([5, 3, 8, 1, 4, 7, 9, None, None, 2, 6], 6, 1, "UUL"),
            ([1, 2, 3, 4, None, None, 5, 6, None, 7], 6, 7, "UUURRL"),
            ([1, 2], 2, 1, "U"),
            ([6, 4, 2, 1, 3, 5], 5, 2, "U"),
            ([1, 3, 2], 1, 3, "L"),
        ],
    )
    def test_get_directions(
        self, root_list: list[int | None], start_value: int, dest_value: int, expected: str
    ):
        result = run_get_directions(Solution, root_list, start_value, dest_value)
        assert_get_directions(result, expected)
