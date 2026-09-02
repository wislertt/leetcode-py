import pytest

from leetcode_py import logged_test

from .helpers import assert_find_all_people, run_find_all_people
from .solution import Solution


class TestFindAllPeopleWithSecret:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, meetings, first_person, expected",
        [
            (6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1, [0, 1, 2, 3, 5]),
            (4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3, [0, 1, 3]),
            (5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1, [0, 1, 2, 3, 4]),
            (2, [[0, 1, 7]], 1, [0, 1]),
            (3, [[1, 2, 5]], 1, [0, 1, 2]),
            (4, [[1, 2, 1], [2, 3, 2], [3, 0, 3]], 1, [0, 1, 2, 3]),
            (4, [[1, 2, 5], [3, 2, 5], [3, 0, 5]], 1, [0, 1, 2, 3]),
            (5, [[1, 2, 1], [3, 4, 1], [2, 3, 1]], 1, [0, 1, 2, 3, 4]),
            (4, [[1, 2, 1], [2, 3, 2]], 1, [0, 1, 2, 3]),
            (4, [[2, 3, 1], [1, 2, 5]], 1, [0, 1, 2]),
            (4, [[1, 2, 1], [1, 2, 3], [2, 3, 3]], 1, [0, 1, 2, 3]),
            (6, [[0, 1, 1], [2, 3, 1], [1, 2, 2]], 5, [0, 1, 2, 5]),
            (3, [[1, 2, 1], [0, 1, 2]], 2, [0, 1, 2]),
            (4, [[1, 2, 5], [2, 3, 5]], 1, [0, 1, 2, 3]),
            (8, [[5, 6, 1], [0, 5, 2], [6, 7, 3], [1, 4, 4], [4, 7, 5]], 1, [0, 1, 4, 5, 7]),
            (7, [[3, 4, 1], [0, 3, 2], [4, 5, 2], [5, 6, 3], [1, 2, 9]], 6, [0, 3, 5, 6]),
        ],
    )
    def test_find_all_people(
        self, n: int, meetings: list[list[int]], first_person: int, expected: list[int]
    ):
        result = run_find_all_people(Solution, n, meetings, first_person)
        assert_find_all_people(result, expected)
