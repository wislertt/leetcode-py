import pytest

from leetcode_py import logged_test

from .helpers import assert_compress, run_compress
from .solution import Solution


class TestStringCompression:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "chars, expected",
        [
            (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"]),
            (["a"], ["a"]),
            (
                ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
                ["a", "b", "1", "2"],
            ),
            (["a", "b"], ["a", "b"]),
            (["a", "a", "a", "b", "b", "b", "c", "c", "c"], ["a", "3", "b", "3", "c", "3"]),
            (["a", "b", "c"], ["a", "b", "c"]),
            (["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "1", "0"]),
            (["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "1", "1"]),
            (["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"], ["a", "1", "2"]),
            (["a", "b", "a", "b", "a", "b"], ["a", "b", "a", "b", "a", "b"]),
            (["A", "A", "a", "a", "a"], ["A", "2", "a", "3"]),
            (["1", "1", "2", "2", "2"], ["1", "2", "2", "3"]),
            (["1", "1", "1"], ["1", "3"]),
            (["a", "1", "a", "1", "a", "1"], ["a", "1", "a", "1", "a", "1"]),
            (["!", "!", "?", "?"], ["!", "2", "?", "2"]),
            (["a", "a", "b", "b"], ["a", "2", "b", "2"]),
        ],
    )
    def test_compress(self, chars: list[str], expected: list[str]):
        result = run_compress(Solution, chars)
        assert_compress(result, expected)
