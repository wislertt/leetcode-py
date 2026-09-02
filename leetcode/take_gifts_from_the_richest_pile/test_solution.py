import pytest

from leetcode_py import logged_test

from .helpers import assert_pick_gifts, run_pick_gifts
from .solution import Solution


class TestTakeGiftsFromTheRichestPile:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "gifts, k, expected",
        [
            ([25, 64, 9, 4, 100], 4, 29),
            ([1, 1, 1, 1], 4, 4),
            ([1], 1, 1),
            ([4], 1, 2),
            ([1000000000], 5, 1),
            ([2, 3, 4, 5], 2, 9),
            ([10, 10, 10], 3, 9),
            ([1, 2, 3], 1000, 3),
            ([999999999, 999999998], 3, 31799),
            ([36, 25, 16], 1, 47),
            ([5, 6, 7, 8, 9], 4, 14),
            ([100, 100], 2, 20),
            ([64, 49, 36, 25, 16, 9], 6, 33),
            ([1, 1], 1000, 2),
            ([86, 8, 168, 82, 191], 6, 32),
            ([105, 1, 132, 28], 4, 19),
            ([128, 169], 10, 2),
            ([78, 25, 130], 10, 3),
        ],
    )
    def test_pick_gifts(self, gifts: list[int], k: int, expected: int):
        result = run_pick_gifts(Solution, gifts, k)
        assert_pick_gifts(result, expected)
