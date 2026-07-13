import pytest

from leetcode_py import logged_test

from .helpers import assert_word_break, run_word_break
from .solution import Solution


class TestTestWordBreakII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, s, word_dict, expected",
        [
            (
                Solution,
                "catsanddog",
                ["cat", "cats", "and", "sand", "dog"],
                ["cats and dog", "cat sand dog"],
            ),
            (
                Solution,
                "pineapplepenapple",
                ["apple", "pen", "applepen", "pine", "pineapple"],
                ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
            ),
            (Solution, "catsandog", ["cats", "dog", "sand", "and", "cat"], []),
            (Solution, "a", ["a"], ["a"]),
            (Solution, "ab", ["a", "b"], ["a b"]),
            (Solution, "ab", ["a"], []),
            (Solution, "leetcode", ["leet", "code"], ["leet code"]),
            (Solution, "leetcode", ["leet", "code", "le", "et"], ["leet code", "le et code"]),
            (Solution, "abc", ["a", "b", "c", "ab", "bc"], ["a b c", "a bc", "ab c"]),
            (Solution, "aa", ["a"], ["a a"]),
            (Solution, "xyz", ["x", "y", "z"], ["x y z"]),
            (Solution, "xyz", ["xyz"], ["xyz"]),
            (Solution, "xyz", ["xy", "z", "x", "yz"], ["xy z", "x yz"]),
            (Solution, "bb", ["a", "b", "bbb", "bbbb"], ["b b"]),
            (Solution, "abcd", ["a", "abc", "b", "cd"], ["a b cd"]),
            (Solution, "aaaa", ["aa", "a"], ["a a a a", "a a aa", "a aa a", "aa a a", "aa aa"]),
            (Solution, "aaaaaaa", ["aaaa", "aaa"], ["aaa aaaa", "aaaa aaa"]),
            (Solution, "abc", ["d"], []),
        ],
    )
    def test_word_break(self, solution_class, s: str, word_dict: list[str], expected: list[str]):
        result = run_word_break(solution_class, s, word_dict)
        assert_word_break(result, expected)
