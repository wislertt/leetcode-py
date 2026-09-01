import pytest

from leetcode_py import logged_test

from .helpers import assert_string_shift, run_string_shift
from .solution import Solution


class TestPerformStringShifts:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, shift, expected",
        [
            ("abc", [[0, 1], [1, 2]], "cab"),
            ("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]], "efgabcd"),
            ("a", [[0, 0]], "a"),
            ("a", [[1, 100]], "a"),
            ("ab", [[1, 1]], "ba"),
            ("ab", [[0, 1]], "ba"),
            ("abc", [[0, 3]], "abc"),
            ("abc", [[1, 4]], "cab"),
            ("abc", [[0, 0], [1, 0]], "abc"),
            ("abcd", [[0, 1], [0, 1], [0, 1], [0, 1]], "abcd"),
            ("xyz", [[1, 5], [0, 3]], "yzx"),
            ("mwkxyz", [[0, 2], [1, 3], [1, 1], [0, 5]], "xyzmwk"),
            ("abcdefghij", [[1, 7], [0, 2], [1, 13], [0, 0]], "cdefghijab"),
            ("zzz", [[0, 100], [1, 100]], "zzz"),
            ("b", [[1, 77], [0, 9], [1, 71], [0, 16]], "b"),
            ("ecaeeaddda", [[1, 30]], "ecaeeaddda"),
            ("bdeabaabca", [[1, 13], [0, 6], [0, 10], [0, 62]], "aabcabdeab"),
            ("a", [[1, 40]], "a"),
            ("decebeaeee", [[1, 52], [0, 76], [1, 70], [1, 47]], "eeedecebea"),
            ("ebbcbbcadc", [[0, 60], [1, 30], [0, 8]], "dcebbcbbca"),
        ],
    )
    def test_string_shift(self, s: str, shift: list[list[int]], expected: str):
        result = run_string_shift(Solution, s, shift)
        assert_string_shift(result, expected)
