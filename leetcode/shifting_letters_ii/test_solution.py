import pytest

from leetcode_py import logged_test

from .helpers import assert_shifting_letters, run_shifting_letters
from .solution import Solution


class TestShiftingLettersII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, shifts, expected",
        [
            ("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace"),
            ("dztz", [[0, 0, 0], [1, 1, 1]], "catz"),
            ("a", [[0, 0, 1]], "b"),
            ("a", [[0, 0, 0]], "z"),
            ("z", [[0, 0, 1]], "a"),
            ("abc", [[0, 2, 1]], "bcd"),
            ("zzz", [[0, 2, 1]], "aaa"),
            ("aaa", [[0, 2, 0]], "zzz"),
            ("abc", [[0, 2, 1], [0, 2, 1], [0, 2, 1]], "def"),
            ("abc", [[0, 2, 0], [0, 2, 0]], "yza"),
            ("abcd", [[0, 1, 1], [2, 3, 1]], "bcde"),
            ("abcd", [[1, 2, 0], [0, 3, 0]], "zzac"),
            ("abcd", [[0, 3, 0], [0, 0, 1], [3, 3, 1]], "aabd"),
            ("dloa", [[0, 2, 0], [0, 1, 0], [0, 2, 0], [3, 3, 1], [0, 0, 1]], "bimb"),
            ("yjljzt", [[4, 5, 0], [2, 2, 0]], "yjkjys"),
            ("hfqsgsps", [[2, 6, 0]], "hfprfros"),
            ("cu", [[0, 1, 0], [0, 0, 0], [1, 1, 0], [1, 1, 0]], "ar"),
            ("raxj", [[0, 2, 1], [0, 0, 0]], "rbyj"),
            ("jijzyv", [[1, 4, 1], [2, 4, 0]], "jjjzyv"),
            ("vxdd", [[1, 2, 0], [3, 3, 1]], "vwce"),
        ],
    )
    def test_shifting_letters(self, s: str, shifts: list[list[int]], expected: str):
        result = run_shifting_letters(Solution, s, shifts)
        assert_shifting_letters(result, expected)
