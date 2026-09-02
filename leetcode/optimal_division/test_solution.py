import pytest

from leetcode_py import logged_test

from .helpers import assert_optimal_division, run_optimal_division
from .solution import Solution


class TestOptimalDivision:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1000, 100, 10, 2], "1000/(100/10/2)"),
            ([2, 3, 4], "2/(3/4)"),
            ([5], "5"),
            ([2], "2"),
            ([1000], "1000"),
            ([2, 3], "2/3"),
            ([1000, 999], "1000/999"),
            ([2, 2], "2/2"),
            ([3, 2, 5], "3/(2/5)"),
            ([1000, 2, 1000], "1000/(2/1000)"),
            ([5, 4, 3, 2], "5/(4/3/2)"),
            ([2, 1000, 2, 1000, 2], "2/(1000/2/1000/2)"),
            ([28, 467, 140, 465, 29, 421, 396, 950], "28/(467/140/465/29/421/396/950)"),
            ([180, 188, 845, 469, 636, 756, 586, 962], "180/(188/845/469/636/756/586/962)"),
            ([462], "462"),
            ([593, 704, 1000], "593/(704/1000)"),
            ([49, 353, 13, 282, 866, 957, 395], "49/(353/13/282/866/957/395)"),
            ([77, 879, 29], "77/(879/29)"),
            ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "2/(3/4/5/6/7/8/9/10/11)"),
        ],
    )
    def test_optimal_division(self, nums: list[int], expected: str):
        result = run_optimal_division(Solution, nums)
        assert_optimal_division(result, expected)
