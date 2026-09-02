import pytest

from leetcode_py import logged_test

from .helpers import assert_count_and_say, run_count_and_say
from .solution import Solution


class TestCountAndSay:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, "1"),
            (2, "11"),
            (3, "21"),
            (4, "1211"),
            (5, "111221"),
            (6, "312211"),
            (7, "13112221"),
            (8, "1113213211"),
            (9, "31131211131221"),
            (10, "13211311123113112211"),
            (11, "11131221133112132113212221"),
            (12, "3113112221232112111312211312113211"),
            (13, "1321132132111213122112311311222113111221131221"),
            (14, "11131221131211131231121113112221121321132132211331222113112211"),
        ],
    )
    def test_count_and_say(self, n: int, expected: str):
        result = run_count_and_say(Solution, n)
        assert_count_and_say(result, expected)
