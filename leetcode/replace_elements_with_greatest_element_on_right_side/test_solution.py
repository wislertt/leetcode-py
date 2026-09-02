import pytest

from leetcode_py import logged_test

from .helpers import assert_replace_elements, run_replace_elements
from .solution import Solution


class TestReplaceElementsWithGreatestElementOnRightSide:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            [[17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1]],
            [[400], [-1]],
            [[1, 2], [2, -1]],
            [[2, 1], [1, -1]],
            [[5, 5, 5], [5, 5, -1]],
            [[1, 2, 3, 4, 5], [5, 5, 5, 5, -1]],
            [[5, 4, 3, 2, 1], [4, 3, 2, 1, -1]],
            [[100000], [-1]],
            [[1, 100000, 2], [100000, 2, -1]],
            [[59835, 92782, 16572, 24076, 42336, 40575], [92782, 42336, 42336, 42336, 40575, -1]],
            [[85607, 47707, 93419, 79445, 39919, 47028], [93419, 93419, 79445, 47028, 47028, -1]],
            [[97545, 33890], [33890, -1]],
            [
                [64355, 65034, 29695, 45777, 76321, 87310, 67281],
                [87310, 87310, 87310, 87310, 87310, 67281, -1],
            ],
            [[9075, 89506], [89506, -1]],
            [
                [86377, 15284, 78692, 2368, 75131, 82337, 58660, 19034],
                [82337, 82337, 82337, 82337, 82337, 58660, 19034, -1],
            ],
        ],
    )
    def test_replace_elements(self, arr: list[int], expected: list[int]):
        result = run_replace_elements(Solution, arr)
        assert_replace_elements(result, expected)
