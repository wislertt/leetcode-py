import pytest

from leetcode_py import logged_test

from .helpers import assert_find_itinerary, run_find_itinerary
from .solution import Solution


class TestReconstructItinerary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tickets, expected",
        [
            (
                [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
                ["JFK", "MUC", "LHR", "SFO", "SJC"],
            ),
            (
                [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
                ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
            ),
            (
                [["JFK", "AAA"], ["AAA", "JFK"], ["JFK", "BBB"], ["BBB", "JFK"]],
                ["JFK", "AAA", "JFK", "BBB", "JFK"],
            ),
            ([["JFK", "LAX"]], ["JFK", "LAX"]),
            ([["JFK", "KKK"], ["KKK", "LLL"]], ["JFK", "KKK", "LLL"]),
            ([["JFK", "ATL"], ["ATL", "JFK"]], ["JFK", "ATL", "JFK"]),
            ([["JFK", "SFO"], ["SFO", "JFK"]], ["JFK", "SFO", "JFK"]),
            ([["JFK", "S"], ["JFK", "T"], ["T", "JFK"]], ["JFK", "T", "JFK", "S"]),
            ([["JFK", "A"], ["A", "B"], ["B", "JFK"], ["JFK", "C"]], ["JFK", "A", "B", "JFK", "C"]),
            (
                [["JFK", "Z"], ["JFK", "A"], ["A", "JFK"], ["JFK", "B"]],
                ["JFK", "A", "JFK", "Z", "B"],
            ),
            (
                [["JFK", "C"], ["C", "JFK"], ["JFK", "A"], ["A", "JFK"]],
                ["JFK", "A", "JFK", "C", "JFK"],
            ),
            ([["JFK", "D"], ["JFK", "A"], ["A", "JFK"]], ["JFK", "A", "JFK", "D"]),
            ([["JFK", "A"], ["A", "C"], ["A", "B"], ["B", "A"]], ["JFK", "A", "B", "A", "C"]),
            ([["JFK", "NRT"], ["JFK", "PEK"], ["PEK", "JFK"]], ["JFK", "PEK", "JFK", "NRT"]),
        ],
    )
    def test_find_itinerary(self, tickets: list[list[str]], expected: list[str]):
        result = run_find_itinerary(Solution, tickets)
        assert_find_itinerary(result, expected)
