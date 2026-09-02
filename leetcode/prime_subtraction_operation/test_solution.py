import pytest

from leetcode_py import logged_test

from .helpers import assert_prime_sub_operation, run_prime_sub_operation
from .solution import Solution


class TestPrimeSubtractionOperation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 9, 6, 10], True),
            ([6, 8, 11, 12], True),
            ([5, 8, 3], False),
            ([1], True),
            ([2], True),
            ([1, 2, 3, 4], True),
            ([4, 3, 2, 1], False),
            ([2, 2], False),
            ([3, 3], True),
            ([5, 5], True),
            ([7, 7], True),
            ([1, 1], False),
            ([999, 1000], True),
            ([1000, 2], False),
            ([5, 11, 5], True),
            ([10, 15, 6], True),
            ([2, 4, 6, 8], True),
            ([20, 21, 22, 23], True),
            ([24, 21, 14, 6, 13, 79, 5], False),
            ([10, 20, 3, 792, 503, 51], False),
            ([506, 236], True),
            ([389, 254, 565, 10, 22], False),
            ([20, 12], True),
            ([18, 24, 795, 924], True),
            ([15, 57, 22, 24, 11], True),
            ([7, 373, 988, 13], True),
        ],
    )
    def test_prime_sub_operation(self, nums: list[int], expected: bool):
        result = run_prime_sub_operation(Solution, nums)
        assert_prime_sub_operation(result, expected)
