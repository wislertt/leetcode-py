import pytest

from leetcode_py import logged_test

from .helpers import assert_read, run_read
from .solution import Solution


class TestReadNCharactersGivenRead4II:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "file, queries, expected",
        [
            ("abc", [1, 2, 1], [1, 2, 0]),
            ("abc", [4, 1], [3, 0]),
            ("abcde", [1, 2, 1], [1, 2, 1]),
            ("abcde", [4, 4, 4], [4, 1, 0]),
            ("a", [1], [1]),
            ("a", [2], [1]),
            ("a", [1, 1, 1], [1, 0, 0]),
            ("ab", [1, 1], [1, 1]),
            ("ab", [2, 1], [2, 0]),
            ("abcdefgh", [3, 3, 3], [3, 3, 2]),
            ("abcdefghij", [4, 4, 4], [4, 4, 2]),
            ("xyz", [5, 1], [3, 0]),
            ("pqrs", [1, 1, 1, 1], [1, 1, 1, 1]),
            ("leetcode", [4, 4, 4, 4], [4, 4, 0, 0]),
            ("abcdef", [2, 2, 2, 2], [2, 2, 2, 0]),
            ("mn", [3, 3], [2, 0]),
            ("abcdefghijk", [1, 4, 4, 4], [1, 4, 4, 2]),
            ("a1b2c3d4e5f6", [4, 4, 4], [4, 4, 4]),
            ("playground", [7, 7, 7], [7, 3, 0]),
        ],
    )
    def test_read(self, file: str, queries: list[int], expected: list[int]):
        result = run_read(Solution, file, queries)
        assert_read(result, expected)
