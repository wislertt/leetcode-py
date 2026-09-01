import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_in_between, run_merge_in_between
from .solution import Solution


class TestMergeInBetweenLinkedLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "list1_vals, a, b, list2_vals, expected_vals",
        [
            (
                [10, 1, 13, 6, 9, 5],
                3,
                4,
                [1000000, 1000001, 1000002],
                [10, 1, 13, 1000000, 1000001, 1000002, 5],
            ),
            (
                [0, 1, 2, 3, 4, 5, 6],
                2,
                5,
                [1000000, 1000001, 1000002, 1000003, 1000004],
                [0, 1, 1000000, 1000001, 1000002, 1000003, 1000004, 6],
            ),
            ([1, 2, 3, 4], 1, 1, [9, 9], [1, 9, 9, 3, 4]),
            ([1, 2, 3, 4], 2, 2, [7], [1, 2, 7, 4]),
            ([5, 6, 7], 1, 1, [1], [5, 1, 7]),
            ([1, 2, 3], 1, 1, [10, 20, 30, 40], [1, 10, 20, 30, 40, 3]),
            ([-1, -2, -3, -4, -5], 1, 3, [0], [-1, 0, -5]),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 6, [100, 200], [0, 1, 2, 100, 200, 7, 8, 9]),
            ([3, 4, 5, 6, 7, 8, 9], 1, 5, [77, 88], [3, 77, 88, 9]),
            ([24, 37, -34, 41, -34, -29], 4, 4, [48], [24, 37, -34, 41, 48, -29]),
            (
                [35, -28, 1, -3, 7, 47, -39, 49, -50],
                7,
                7,
                [-40, -16, 8, 49],
                [35, -28, 1, -3, 7, 47, -39, -40, -16, 8, 49, -50],
            ),
            (
                [-42, -47, -22, -44, -49, -42, 13, 13, -41],
                6,
                6,
                [44, 3],
                [-42, -47, -22, -44, -49, -42, 44, 3, 13, -41],
            ),
            ([19, 12, 9, -3, 22, -26], 3, 3, [27, -23], [19, 12, 9, 27, -23, 22, -26]),
            (
                [-43, 25, 13, 30, 32, 44, -19, 1, -24],
                1,
                3,
                [28, -42, -26, -42],
                [-43, 28, -42, -26, -42, 32, 44, -19, 1, -24],
            ),
        ],
    )
    def test_merge_in_between(
        self, list1_vals: list[int], a: int, b: int, list2_vals: list[int], expected_vals: list[int]
    ):
        result = run_merge_in_between(Solution, list1_vals, a, b, list2_vals)
        assert_merge_in_between(result, expected_vals)
