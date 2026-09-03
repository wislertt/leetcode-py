import pytest

from leetcode_py import logged_test

from .helpers import assert_average_of_levels, run_average_of_levels
from .solution import Solution


class TestAverageOfLevelsInBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [3.0, 14.5, 11.0]),
            ([3, 9, 20, 15, 7], [3.0, 14.5, 11.0]),
            ([1], [1.0]),
            ([1, 2, 3], [1.0, 2.5]),
            ([0], [0.0]),
            ([-1, -2, -3], [-1.0, -2.5]),
            ([2147483647, 2147483647, 2147483647], [2147483647.0, 2147483647.0]),
            ([-2147483648], [-2147483648.0]),
            ([1, None, 2, None, 3], [1.0, 2.0, 3.0]),
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                [5.0, 6.0, 9.3333333333, 3.3333333333],
            ),
            ([1, 2, 2, 3, 3, 3, 3], [1.0, 2.0, 3.0]),
            ([10, 5, 15, None, 6, 12, 20], [10.0, 10.0, 12.6666666667]),
            ([100, 50, 150, 25, 75, 125, 175], [100.0, 100.0, 100.0]),
            ([7, -8, 9, None, 10, None, -11], [7.0, 0.5, -0.5]),
            (
                [9, -62, 2147483647, -63, None, None, 0, None, -80],
                [9.0, 1073741792.5, -31.5, -80.0],
            ),
            ([-5, -42, 91, -2147483648, 31, -8, -2147483648], [-5.0, 24.5, -1073741818.25]),
            ([3, -59, -2147483648], [3.0, -1073741853.5]),
            ([9, -47, -49, None, -40], [9.0, -48.0, -40.0]),
        ],
    )
    def test_average_of_levels(self, root_list: list[int | None], expected: list[float]):
        result = run_average_of_levels(Solution, root_list)
        assert_average_of_levels(result, expected)
