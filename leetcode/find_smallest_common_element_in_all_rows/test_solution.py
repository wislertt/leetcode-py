import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_common_element, run_smallest_common_element
from .solution import Solution


class TestFindSmallestCommonElementInAllRows:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]], 5),
            ([[1, 2, 3], [2, 3, 4], [2, 3, 5]], 2),
            ([[7]], 7),
            ([[1, 2, 3]], 1),
            ([[1], [2], [3]], -1),
            ([[5], [5], [5]], 5),
            ([[1, 2], [3, 4]], -1),
            ([[1, 2, 3], [1, 4, 5], [1, 6, 7]], 1),
            ([[1, 2, 9], [3, 4, 9], [5, 6, 9]], 9),
            ([[9999, 10000], [9998, 10000], [9997, 10000]], 10000),
            ([[1, 2], [1, 3]], 1),
            ([[2, 4], [1, 4], [3, 4]], 4),
            ([[10, 20, 30], [15, 20, 35], [20, 40, 50]], 20),
            ([[1, 3, 5, 7], [2, 3, 6, 7], [3, 4, 5, 7], [1, 2, 3, 7]], 3),
            ([[4, 5], [1, 5], [2, 5], [3, 5]], 5),
            ([[2, 3], [1, 3], [3, 4]], 3),
            (
                [
                    [11, 12, 28, 54, 56],
                    [7, 24, 36, 38, 58],
                    [31, 45, 49, 52, 55],
                    [10, 19, 20, 27, 39],
                ],
                -1,
            ),
            ([[7, 11, 34], [26, 34, 40], [16, 26, 34], [26, 34, 49]], 34),
            ([[1, 25, 38], [1, 5, 25], [1, 14, 25], [1, 22, 25], [1, 25, 31]], 1),
            (
                [
                    [2, 9, 14, 24, 25],
                    [9, 12, 20, 29, 42],
                    [3, 9, 29, 30, 37],
                    [9, 21, 29, 38, 39],
                    [6, 7, 9, 23, 29],
                ],
                9,
            ),
        ],
    )
    def test_smallest_common_element(self, mat: list[list[int]], expected: int):
        result = run_smallest_common_element(Solution, mat)
        assert_smallest_common_element(result, expected)
