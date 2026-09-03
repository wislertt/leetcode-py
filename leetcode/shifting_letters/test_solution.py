import pytest

from leetcode_py import logged_test

from .helpers import assert_shifting_letters, run_shifting_letters
from .solution import Solution


class TestShiftingLetters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, shifts, expected",
        [
            ("abc", [3, 5, 9], "rpl"),
            ("aaa", [1, 2, 3], "gfd"),
            ("a", [1], "b"),
            ("a", [0], "a"),
            ("a", [25], "z"),
            ("z", [1], "a"),
            ("zz", [1, 1], "ba"),
            ("abc", [0, 0, 0], "abc"),
            ("abc", [26, 26, 26], "abc"),
            ("a", [1000000000], "m"),
            ("z", [999999999], "k"),
            ("abcdef", [1, 2, 3, 4, 5, 6], "vvuspl"),
            ("leetcode", [1, 2, 3, 4, 5, 6, 7, 8], "vnlxcjsm"),
            ("xyzz", [1000000000, 1000000000, 1000000000, 1000000000], "tixl"),
            ("cba", [1000000000, 999999998, 3], "bod"),
            ("znzd", [0, 26, 0, 27], "aoae"),
            ("speg", [0, 0, 1, 25], "spef"),
            ("ii", [1000000000, 25], "th"),
        ],
    )
    def test_shifting_letters(self, s: str, shifts: list[int], expected: str):
        result = run_shifting_letters(Solution, s, shifts)
        assert_shifting_letters(result, expected)
