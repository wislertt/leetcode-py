import pytest

from leetcode_py import logged_test

from .helpers import assert_triplet_count, run_triplet_count
from .solution import Solution


class TestCountTripletsWithEvenXorSetBitsI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, c, expected",
        [
            ([1], [2], [3], 1),
            ([1, 1], [2, 3], [1, 5], 4),
            ([84, 52], [48], [32, 85, 18, 20], 2),
            ([52, 24, 41], [3, 38, 87], [58, 48, 68, 65, 27], 25),
            ([76], [69, 21, 22, 74, 23], [95, 7, 37, 21, 58], 11),
            ([39, 17, 18], [63, 51, 20, 60, 92], [73, 54], 15),
            ([93, 43, 14, 38, 13], [26, 94, 92], [77, 70], 15),
            ([11, 32], [27, 84, 49, 44], [45, 56], 8),
            ([81], [60, 56], [18, 87], 2),
            ([35, 93, 50, 77, 83], [22, 61], [91, 7, 6, 78, 75], 26),
            ([78], [23, 18, 95, 23], [79, 75, 6, 57], 12),
            ([21, 22, 69], [69], [13, 74, 63, 11], 3),
            ([45, 43], [91], [98, 8, 76, 2], 8),
            ([26, 33, 71, 38], [93, 32, 30, 75, 97], [87, 81, 74, 8, 10], 50),
            ([44, 38], [94, 86], [54], 2),
            ([74, 75], [30, 79], [17], 2),
            ([0], [0], [0], 1),
            ([0, 0, 0], [0, 0], [0], 6),
            ([100], [100], [100], 0),
            ([1, 2, 4, 8], [1, 2, 4, 8], [1, 2, 4, 8], 0),
            ([7], [7], [7], 0),
        ],
    )
    def test_triplet_count(self, a: list[int], b: list[int], c: list[int], expected: int):
        result = run_triplet_count(Solution, a, b, c)
        assert_triplet_count(result, expected)
