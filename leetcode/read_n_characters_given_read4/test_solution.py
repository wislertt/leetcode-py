import pytest

from leetcode_py import logged_test

from .helpers import assert_read, run_read
from .solution import Solution


class TestReadNCharactersGivenRead4:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "file, n, expected",
        [
            ("abc", 4, 3),
            ("abcde", 5, 5),
            ("abcdABCD1234", 12, 12),
            ("leetcode", 5, 5),
            ("a", 1, 1),
            ("ab", 1, 1),
            ("abc", 1, 1),
            ("abcd", 4, 4),
            ("abcdef", 4, 4),
            ("abcdefg", 3, 3),
            ("abcdefgh", 10, 8),
            ("abcdefghi", 9, 9),
            ("abcde", 4, 4),
            ("xy", 1000, 2),
            ("leet", 1, 1),
            ("a1b2c3d4e5", 10, 10),
            ("playground", 7, 7),
        ],
    )
    def test_read(self, file: str, n: int, expected: int):
        result = run_read(Solution, file, n)
        assert_read(result, expected)
