import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_ways, run_number_of_ways
from .solution import Solution


class TestHandshakesThatDontCross:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num_people, expected",
        [
            (2, 1),
            (4, 2),
            (6, 5),
            (8, 14),
            (10, 42),
            (12, 132),
            (14, 429),
            (16, 1430),
            (18, 4862),
            (20, 16796),
            (22, 58786),
            (24, 208012),
            (30, 9694845),
            (40, 564120378),
            (60, 475387402),
            (100, 265470434),
            (500, 217193473),
            (1000, 591137401),
        ],
    )
    def test_number_of_ways(self, num_people: int, expected: int):
        result = run_number_of_ways(Solution, num_people)
        assert_number_of_ways(result, expected)
