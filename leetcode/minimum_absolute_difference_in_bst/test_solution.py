import pytest

from leetcode_py import logged_test

from .helpers import assert_get_minimum_difference, run_get_minimum_difference
from .solution import Solution


class TestMinimumAbsoluteDifferenceInBst:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([4, 2, 6, 1, 3], 1),
            ([1, 0, 48, None, None, 12, 49], 1),
            ([10, 5], 5),
            ([2, 1, 4], 1),
            ([5, 3, 7, 1, 4], 1),
            ([10, 5, 20, 3, 7, 15, 30], 2),
            ([40, None, 70, 60, 80], 10),
            ([1, None, 3, 2], 1),
            ([9, 4, 15, 1, 6, 12, 20], 2),
            ([0, None, 100000], 100000),
            ([27, None, 40, 30, 45], 3),
            ([50, 20, 80, 10, 35, 70, 95], 10),
            ([7, 3, 15, None, None, 9, 20], 2),
            ([100, 50, 200, 25, 75, 150, 250], 25),
            ([54, 46, 382, None, None, 285, None, 114, 310, None, 250], 8),
            ([199, 87, 325, 17, None, 285, 360, None, 28, 259], 11),
            ([379, 149, 389, None, 347, None, 398, 176], 9),
            ([11, None, 21], 10),
            ([67, 63, 86, 8, None, None, 215, None, None, 143, 374], 4),
            ([104, 7, 130, 6, None, None, 138, None, None, None, 313], 1),
        ],
    )
    def test_get_minimum_difference(self, root_list: list[int | None], expected: int):
        result = run_get_minimum_difference(Solution, root_list)
        assert_get_minimum_difference(result, expected)
