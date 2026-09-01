import pytest

from leetcode_py import logged_test

from .helpers import assert_count_seniors, run_count_seniors
from .solution import Solution


class TestNumberOfSeniorCitizens:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "details, expected",
        [
            (["7000000000M7511", "7000000137F9218", "7000000274O4025"], 2),
            (["7000000000M2011", "7000000137F5618"], 0),
            (["7000000000M6111"], 1),
            (["7000000000M6011"], 0),
            (["7000000000M5911", "7000000137F6018", "7000000274O6125", "7000000411M9932"], 2),
            (["7000000000M0011", "7000000137F0118", "7000000274O9925"], 1),
            (["7000000000M6111", "7000000137F6218", "7000000274O6325", "7000000411M6432"], 4),
            (["7000000000M1011", "7000000137F2018", "7000000274O3025", "7000000411M4032"], 0),
            (["7000000000M7011", "7000000137F7118", "7000000274O7225", "7000000411M8032"], 4),
            (["7000000000M6111", "7000000137F6018"], 1),
            (["7000000000M1311", "7000000137F6118", "7000000274O4525", "7000000411M6132"], 2),
            (["7000000000M9911", "7000000137F0018"], 1),
            (["1234567890M6599"], 1),
            (["9876543210M1600"], 0),
            (["1111111111O6101", "2222222222F3523", "3333333333M7045"], 2),
            (["4567890123M6012", "5678901234F6134", "6789012345O6056", "7890123456M6178"], 2),
        ],
    )
    def test_count_seniors(self, details: list[str], expected: int):
        result = run_count_seniors(Solution, details)
        assert_count_seniors(result, expected)
