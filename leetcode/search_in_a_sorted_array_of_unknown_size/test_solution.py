import pytest

from leetcode_py import logged_test

from .helpers import assert_search, run_search
from .solution import Solution


class TestSearchInASortedArrayOfUnknownSize:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "secret, target, expected",
        [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
            ([-1, 0, 3, 5, 9, 12], 12, 5),
            ([-1, 0, 3, 5, 9, 12], -1, 0),
            ([5], 5, 0),
            ([5], 4, -1),
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 5, 4),
            ([-10000, -9999, -1, 0, 1], 0, 3),
            ([-10000, -9999, -1, 0, 1], 2, -1),
            ([2, 5], 2, 0),
            ([2, 5], 6, -1),
            ([-5, -3, 0, 7, 8, 21, 40], 40, 6),
            ([-5, -3, 0, 7, 8, 21, 40], -6, -1),
            ([-5, -3, 0, 7, 8, 21, 40], 20, -1),
            ([-9032, -5538], -3583, -1),
            ([-7448, -1253, 3702, 5332, 8829], 8829, 4),
            ([-7409, -5206, 5751], 2330, -1),
        ],
    )
    def test_search(self, secret: list[int], target: int, expected: int):
        result = run_search(Solution, secret, target)
        assert_search(result, expected)
