import pytest

from leetcode_py import logged_test

from .helpers import assert_max_product, run_max_product
from .solution import Solution


class TestMaximumProductOfWordLengths:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
            (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
            (["a", "aa", "aaa", "aaaa"], 0),
            (["ab", "cd"], 4),
            (["ab", "abc"], 0),
            (["a", "b"], 1),
            (["xy", "yz", "xz"], 0),
            (["abc", "def", "ghi"], 9),
            (["abcd", "efgh", "abc"], 16),
            (["aaaa", "bbbb", "cc"], 16),
            (["aabb", "bbaa", "ccdd"], 16),
            (["hello", "world", "leetcode"], 0),
            (["abc", "xyz", "abcd"], 12),
            (["qwerty", "asdfg", "zxcvb"], 30),
            (["aa", "bb", "cc", "ab"], 4),
            (["a", "a"], 0),
            (["abcdefg", "hijklmn", "opqrstu", "vwxyz"], 49),
            (["book", "keep", "flag"], 16),
            (["abcde", "fghij", "klmno", "pqrst"], 25),
            (["abc", "abc"], 0),
        ],
    )
    def test_max_product(self, words: list[str], expected: int):
        result = run_max_product(Solution, words)
        assert_max_product(result, expected)
