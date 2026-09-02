import pytest

from leetcode_py import logged_test

from .helpers import assert_max_number_of_apples, run_max_number_of_apples
from .solution import Solution


class TestHowManyApplesCanYouPutIntoTheBasket:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "weight, expected",
        [
            ([100, 200, 150, 1000], 4),
            ([900, 950, 800, 1000, 700, 800], 5),
            ([1], 1),
            ([1000], 1),
            ([1000, 1000, 1000, 1000, 1000], 5),
            ([1000, 1000, 1000, 1000, 1000, 1000], 5),
            ([1, 1, 1], 3),
            ([1000, 1000, 1000, 1000, 1000, 1], 5),
            ([1, 2, 3, 4, 5], 5),
            ([999, 999, 999, 999, 999, 999], 5),
            ([500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500], 10),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
            ([1000, 1000, 1000, 1000, 999], 5),
            ([999, 999, 999, 999, 999, 1], 6),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1000], 10),
            ([600, 600, 600, 600, 600, 600, 600, 600, 900], 8),
            ([258, 484, 620], 3),
            ([762, 367, 240, 45, 504, 700, 643, 637, 657], 9),
            ([34, 96, 553, 315, 35, 6], 6),
            ([240, 844, 984, 929, 224], 5),
        ],
    )
    def test_max_number_of_apples(self, weight: list[int], expected: int):
        result = run_max_number_of_apples(Solution, weight)
        assert_max_number_of_apples(result, expected)
