import pytest

from leetcode_py import logged_test

from .helpers import assert_max_satisfied, run_max_satisfied
from .solution import Solution


class TestGrumpyBookstoreOwner:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "customers, grumpy, minutes, expected",
        [
            ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16),
            ([1], [0], 1, 1),
            ([4, 10, 10], [1, 1, 0], 2, 24),
            ([1], [1], 1, 1),
            ([0], [1], 1, 0),
            ([2, 6, 6, 2], [0, 0, 1, 1], 2, 16),
            ([9, 10, 4, 5], [1, 0, 1, 1], 1, 19),
            ([5, 8, 2, 9, 1], [0, 1, 0, 1, 0], 2, 17),
            ([3, 7, 1, 4, 2, 6], [1, 1, 1, 1, 1, 1], 6, 23),
            ([3, 7, 1, 4, 2, 6], [1, 1, 1, 1, 1, 1], 1, 7),
            ([10, 1, 1, 10], [0, 1, 1, 0], 2, 22),
            ([7, 7, 7, 7], [1, 0, 1, 0], 1, 21),
            ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0], 2, 15),
            ([1000, 0, 1000], [1, 0, 1], 1, 1000),
            ([2, 3, 1, 5, 4, 6, 8, 2], [1, 0, 1, 0, 1, 0, 1, 0], 3, 28),
        ],
    )
    def test_max_satisfied(
        self, customers: list[int], grumpy: list[int], minutes: int, expected: int
    ):
        result = run_max_satisfied(Solution, customers, grumpy, minutes)
        assert_max_satisfied(result, expected)
