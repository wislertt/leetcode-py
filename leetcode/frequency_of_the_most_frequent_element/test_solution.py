import pytest

from leetcode_py import logged_test

from .helpers import assert_max_frequency, run_max_frequency
from .solution import Solution


class TestFrequencyOfTheMostFrequentElement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 4], 5, 3),
            ([1, 4, 8, 13], 5, 2),
            ([3, 9, 6], 2, 1),
            ([1], 1, 1),
            ([5, 5, 5, 5], 3, 4),
            ([1, 2, 3, 4, 5], 10, 5),
            ([2, 2, 2], 1, 3),
            ([1, 100000], 99999, 2),
            ([1, 100000], 99998, 1),
            ([10, 9, 2, 8], 4, 3),
            ([9930, 9923, 9910, 9983, 9996], 2, 1),
            ([10000, 1, 1, 1, 1], 4, 4),
            ([1, 4, 4, 4, 6], 3, 4),
            ([1, 2, 4], 1, 2),
            ([19712, 6521], 35812, 2),
            ([73672, 21237, 17016, 79817, 64460, 50178, 30141, 3864], 79440, 4),
        ],
    )
    def test_max_frequency(self, nums: list[int], k: int, expected: int):
        result = run_max_frequency(Solution, nums, k)
        assert_max_frequency(result, expected)
