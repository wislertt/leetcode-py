import pytest

from leetcode_py import logged_test

from .helpers import assert_dest_city, run_dest_city
from .solution import Solution


class TestTestDestinationCity:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "paths, expected",
        [
            ([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]], "Sao Paulo"),
            ([["B", "C"], ["D", "B"], ["C", "A"]], "A"),
            ([["A", "Z"]], "Z"),
            ([["X", "Y"], ["Z", "X"]], "Y"),
            ([["p", "q"], ["q", "r"]], "r"),
            ([["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]], "Delta"),
            ([["New York", "Lima"]], "Lima"),
            ([["a b", "c d"]], "c d"),
            ([["Dubai", "C"], ["Peru", "Dubai"], ["C", "NYC"]], "NYC"),
            (
                [
                    ["Peru", "NYC"],
                    ["NYC", "Tokyo"],
                    ["Tokyo", "LA"],
                    ["LA", "Cairo"],
                    ["Dubai", "Peru"],
                ],
                "Cairo",
            ),
            ([["LA", "H"]], "H"),
            ([["NYC", "Miami"], ["B", "NYC"], ["Miami", "A"], ["A", "Tokyo"]], "Tokyo"),
            ([["Rome", "Cairo"], ["Cairo", "I"], ["I", "Miami"], ["M", "Rome"]], "Miami"),
            (
                [
                    ["M", "F"],
                    ["Paris", "Cairo"],
                    ["Cairo", "M"],
                    ["D", "Tokyo"],
                    ["Tokyo", "Paris"],
                ],
                "F",
            ),
        ],
    )
    def test_dest_city(self, paths: list[list[str]], expected: str):
        result = run_dest_city(Solution, paths)
        assert_dest_city(result, expected)
