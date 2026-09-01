import pytest

from leetcode_py import logged_test

from .helpers import assert_maximize_sweetness, run_maximize_sweetness
from .solution import Solution


class TestDivideChocolate:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sweetness, k, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 6),
            ([5, 6, 7, 8, 9, 1, 2, 3, 4], 8, 1),
            ([1, 2, 2, 1, 2, 2, 1, 2, 2], 2, 5),
            ([1], 0, 1),
            ([10], 0, 10),
            ([5, 5], 0, 10),
            ([3, 1, 4], 2, 1),
            ([7, 2, 9, 5], 3, 2),
            ([1, 2, 3, 4], 1, 4),
            ([4, 3, 2, 1], 1, 4),
            ([2, 2, 2, 2], 2, 2),
            ([9, 9, 9, 9, 9], 4, 9),
            ([1, 1, 1, 1, 1, 1], 2, 2),
            ([8, 1, 1, 8], 1, 9),
            ([100000], 0, 100000),
            ([100000, 100000, 100000], 2, 100000),
            ([6, 1, 2, 7, 3, 5], 1, 9),
            ([5, 4, 3, 2, 1, 5, 4, 3, 2, 1], 3, 6),
            ([19, 9, 2, 14, 13, 8, 17, 6], 5, 8),
            ([12, 7, 20, 11, 19, 12], 1, 39),
            ([9, 6, 2, 7, 15, 11, 16, 12], 4, 11),
            ([5, 19, 8, 6, 7, 5, 2, 9, 17, 5], 4, 11),
            ([4, 5], 1, 4),
            ([8, 14], 0, 22),
            ([14, 6, 4, 1, 6, 16, 1, 19, 11], 5, 7),
            ([20, 4, 18, 4], 3, 4),
            ([10, 1, 17, 13, 13, 19], 1, 32),
            ([13, 16, 11], 1, 13),
            ([1, 2, 4, 14, 10], 0, 31),
            ([3, 6, 11], 2, 3),
        ],
    )
    def test_maximize_sweetness(self, sweetness: list[int], k: int, expected: int):
        result = run_maximize_sweetness(Solution, sweetness, k)
        assert_maximize_sweetness(result, expected)
