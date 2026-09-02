import pytest

from leetcode_py import logged_test

from .helpers import assert_min_subarray, run_min_subarray
from .solution import Solution


class TestMakeSumDivisibleByP:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, p, expected",
        [
            ([1000000000], 1000000000, 0),
            ([5], 3, -1),
            ([369036771], 726693104, -1),
            ([23, 38], 8, -1),
            ([44913052, 744535641], 9, -1),
            ([1, 2, 3], 3, 0),
            ([1, 2, 3], 7, -1),
            ([4, 4, 2], 7, -1),
            ([9, 9, 9], 3, 0),
            ([408969450, 275894403, 989966710], 1, 0),
            ([29, 23, 10], 576464984, -1),
            ([3, 1, 4, 2], 6, 1),
            ([6, 3, 5, 2], 9, 2),
            ([3, 1, 2, 4], 10, 0),
            ([2, 4, 6, 8], 5, 0),
            ([7, 4, 5, 1, 2], 6, 1),
            ([341414726, 237972821, 733208358, 718392026, 883354863], 281902445, -1),
            ([37, 16, 29, 49, 37, 15], 6, 1),
            ([8, 32, 17, 40, 28, 17, 96], 24, 6),
            ([13, 32, 48, 25, 15, 36, 22], 142850692, -1),
        ],
    )
    def test_min_subarray(self, nums: list[int], p: int, expected: int):
        result = run_min_subarray(Solution, nums, p)
        assert_min_subarray(result, expected)
