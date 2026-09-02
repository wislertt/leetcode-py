import pytest

from leetcode_py import logged_test

from .helpers import assert_leads_to_destination, run_leads_to_destination
from .solution import Solution


class TestAllPathsFromSourceLeadToDestination:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, source, destination, expected",
        [
            (3, [[0, 1], [0, 2]], 0, 2, False),
            (4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3, False),
            (4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3, True),
            (1, [], 0, 0, True),
            (2, [[0, 1], [0, 1]], 0, 1, True),
            (2, [[0, 0]], 0, 1, False),
            (3, [[0, 1], [1, 2], [2, 2]], 0, 2, False),
            (5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0, 4, True),
            (4, [[0, 1], [1, 2], [2, 0]], 0, 3, False),
            (3, [[0, 1], [0, 2], [1, 2]], 0, 2, True),
            (2, [[0, 1]], 1, 1, True),
            (4, [[0, 1], [0, 3], [1, 2], [2, 1], [3, 3]], 0, 3, False),
        ],
    )
    def test_leads_to_destination(
        self, n: int, edges: list[list[int]], source: int, destination: int, expected: bool
    ):
        result = run_leads_to_destination(Solution, n, edges, source, destination)
        assert_leads_to_destination(result, expected)
