import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_moves, run_minimum_moves
from .solution import Solution


class TestPalindromeRemoval:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2], 2),
            ([1, 3, 4, 1, 5], 3),
            ([1], 1),
            ([1, 1], 1),
            ([2, 2, 2], 1),
            ([1, 2, 1], 1),
            ([1, 2, 2, 1], 1),
            ([1, 2, 3], 3),
            ([1, 2, 3, 2, 1], 1),
            ([1, 3, 2, 3, 1], 1),
            ([1, 2, 1, 2], 2),
            ([1, 4, 1, 1, 4, 1], 1),
            ([3, 3, 3, 3, 3, 3, 3], 1),
            ([1, 20, 1, 20, 1], 1),
            ([4, 1, 4, 5, 1], 3),
            ([2, 1, 2, 1, 2, 2, 1], 2),
            ([1, 2, 3, 4, 5], 5),
            ([1, 1, 2, 2, 1, 1], 1),
            ([7, 8, 7, 8, 7], 1),
            ([5, 5, 1, 5, 5, 9, 9, 5], 3),
            ([1, 3, 1, 3, 3, 2], 3),
            ([1, 3, 3, 3, 1, 2], 2),
            ([2, 3, 2, 2, 1, 1], 3),
            ([1, 2, 2, 2, 2, 3, 1, 3], 3),
            ([2, 1, 2, 1, 3, 2, 3], 3),
            ([3, 3, 3, 1, 1, 1], 2),
            ([2, 1, 2, 1, 1, 2, 1, 3], 3),
            ([3, 1, 1, 1, 3, 3, 2, 3], 2),
            ([1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3], 2),
            ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1),
            ([19, 13, 6, 17, 14, 15, 19, 2, 13, 12, 13, 9, 6, 10, 1], 11),
            (
                [
                    3,
                    4,
                    1,
                    2,
                    4,
                    2,
                    4,
                    1,
                    3,
                    4,
                    1,
                    3,
                    2,
                    3,
                    2,
                    3,
                    4,
                    2,
                    3,
                    2,
                    2,
                    1,
                    3,
                    4,
                    4,
                    3,
                    3,
                    2,
                    2,
                    1,
                ],
                9,
            ),
        ],
    )
    def test_minimum_moves(self, arr: list[int], expected: int):
        result = run_minimum_moves(Solution, arr)
        assert_minimum_moves(result, expected)
