import pytest

from leetcode_py import logged_test

from .helpers import assert_predict_party_victory, run_predict_party_victory
from .solution import Solution


class TestDota2Senate:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "senate, expected",
        [
            ("RD", "Radiant"),
            ("RDD", "Dire"),
            ("R", "Radiant"),
            ("D", "Dire"),
            ("RRR", "Radiant"),
            ("DDD", "Dire"),
            ("RRDDD", "Radiant"),
            ("DDRRR", "Dire"),
            ("DR", "Dire"),
            ("DRDR", "Dire"),
            ("RDRD", "Radiant"),
            ("RRRDDD", "Radiant"),
            ("DDDRRR", "Dire"),
            ("RDRDD", "Radiant"),
            ("DRRDD", "Dire"),
        ],
    )
    def test_predict_party_victory(self, senate: str, expected: str):
        result = run_predict_party_victory(Solution, senate)
        assert_predict_party_victory(result, expected)
