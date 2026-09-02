import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_ways, run_number_of_ways
from .solution import Solution


class TestNumberOfWaysToDivideALongCorridor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "corridor, expected",
        [
            ("SSPPSPS", 3),
            ("PPSPSP", 1),
            ("S", 0),
            ("P", 0),
            ("PP", 0),
            ("SS", 1),
            ("SPS", 1),
            ("SSPPSS", 3),
            ("SSSS", 1),
            ("PPP", 0),
            ("PSSP", 1),
            ("SSPPPSS", 4),
            ("SSPSPSPPSS", 6),
            ("PPPPSP", 0),
            ("SSPPSSS", 0),
            ("PSSSSSSPSSSPP", 0),
            ("PPPSPSPSSP", 2),
            ("SSPPSSSPP", 0),
            ("SPSSS", 1),
            ("PSPPSSSPPSSPSPPS", 6),
            ("PSPSSPPSPSSPS", 0),
            ("SSSP", 0),
            ("SSSPPSPSSPSSPSP", 0),
            ("SSSPPPPP", 0),
            ("SSSSSPPPPPP", 0),
        ],
    )
    def test_number_of_ways(self, corridor: str, expected: int):
        result = run_number_of_ways(Solution, corridor)
        assert_number_of_ways(result, expected)
