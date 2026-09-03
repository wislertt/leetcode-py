import pytest

from leetcode_py import logged_test

from .helpers import assert_find_contest_match, run_find_contest_match
from .solution import Solution


class TestOutputContestMatches:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, "(1,2)"),
            (4, "((1,4),(2,3))"),
            (8, "(((1,8),(4,5)),((2,7),(3,6)))"),
            (16, "((((1,16),(8,9)),((4,13),(5,12))),(((2,15),(7,10)),((3,14),(6,11))))"),
            (32, 148),
            (64, 308),
            (128, 657),
            (256, 1425),
            (512, 2961),
            (1024, 6058),
            (2048, 13226),
            (4096, 27562),
        ],
    )
    def test_find_contest_match(self, n: int, expected: str | int):
        result = run_find_contest_match(Solution, n)
        assert_find_contest_match(result, n, expected)
