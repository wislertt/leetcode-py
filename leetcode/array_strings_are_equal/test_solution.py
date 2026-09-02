import pytest

from leetcode_py import logged_test

from .helpers import assert_array_strings_are_equal, run_array_strings_are_equal
from .solution import Solution


class TestArrayStringsAreEqual:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            (["ab", "c"], ["a", "bc"], True),
            (["a", "cb"], ["ab", "c"], False),
            (["abc", "d", "defg"], ["abcddefg"], True),
            (["a"], ["a"], True),
            (["a"], ["b"], False),
            (["ab", "cd"], ["abcd"], True),
            (["abc"], ["ab", "c"], True),
            (["abc"], ["ab", "d"], False),
            (["ab", "ab"], ["aba", "b"], True),
            (["ab", "ab"], ["aba", "c"], False),
            (["xyz", "abc"], ["xy", "zabc"], True),
            (["p", "q", "r"], ["pqr"], True),
            (["p", "q", "r"], ["pqs"], False),
            (["aa", "bb", "cc"], ["aabb", "cc"], True),
            (["aa", "bb", "cc"], ["aac", "bb", "cc"], False),
            (["abc", "def"], ["a", "bc", "de", "f"], True),
        ],
    )
    def test_array_strings_are_equal(self, word1: list[str], word2: list[str], expected: bool):
        result = run_array_strings_are_equal(Solution, word1, word2)
        assert_array_strings_are_equal(result, expected)
