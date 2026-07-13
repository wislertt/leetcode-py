import pytest

from leetcode_py import logged_test

from .helpers import assert_min_extra_char, run_min_extra_char
from .solution import Solution


class TestTestExtraCharactersInAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, dictionary, expected",
        [
            ("leetscode", ["leet", "code", "leetcode"], 1),
            ("sayhelloworld", ["hello", "world"], 3),
            ("leetcode", ["leet", "code"], 0),
            ("hello", ["hello"], 0),
            ("a", ["b"], 1),
            ("a", ["a"], 0),
            ("abc", ["a", "b", "c"], 0),
            ("abc", ["d", "e"], 3),
            ("aaaa", ["aa"], 0),
            ("aaaa", ["aaa"], 1),
            ("xyz", ["q"], 3),
            ("binary", ["bin", "ary"], 0),
            ("abcd", ["ab", "cd", "abcd"], 0),
            ("ababab", ["ab", "ba"], 0),
            ("xxx", ["xx"], 1),
        ],
    )
    def test_min_extra_char(self, s: str, dictionary: list[str], expected: int):
        result = run_min_extra_char(Solution, s, dictionary)
        assert_min_extra_char(result, expected)
