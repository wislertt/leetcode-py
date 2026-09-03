import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_superstring, run_shortest_superstring
from .solution import Solution


class TestFindTheShortestSuperstring:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["alex", "loves", "leetcode"], 17),
            (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], 16),
            (["a"], 1),
            (["ab"], 2),
            (["abcdef"], 6),
            (["ab", "ba"], 3),
            (["abc", "cde"], 5),
            (["abab", "baba"], 5),
            (["cata", "tac"], 5),
            (["bbaba", "ababab"], 8),
            (["aa", "ab", "ba"], 4),
            (["aaa", "aab", "baa", "ccc"], 8),
            (["catg", "gcta", "ttca"], 9),
            (["ctaagt", "gcta", "atgcatc"], 14),
            (["al", "exl", "leva"], 7),
            (["xyxyx", "yxyxy"], 6),
            (["bd", "ca", "cd", "ac"], 6),
            (["bb", "dc", "bd", "db"], 5),
            (["cb", "ba", "ac", "bc"], 5),
            (["cc", "bd"], 4),
            (["dc", "cc"], 3),
            (["bc", "db"], 3),
            (["dc", "dd", "bc"], 5),
            (["da", "db", "bc"], 5),
            (["ba", "db"], 3),
            (["bc", "cc", "ba", "ac"], 6),
            (["ab", "cb"], 4),
            (["ac", "cc", "aa"], 4),
            (["bc", "ab", "db"], 5),
            (["ac", "ca", "dc", "cc"], 5),
            (["cc", "ac", "da"], 4),
            (["bc", "bd", "cb", "aa"], 6),
            (["ad", "da", "cb", "cd"], 6),
            (["aa", "ad", "da", "dc"], 5),
            (["ac", "ad", "ca", "da"], 5),
            (["cb", "ba", "aa", "bd"], 6),
            (["dd", "ba", "cb"], 5),
            (["cc", "ad"], 4),
            (["cd", "db", "cc", "ac"], 5),
            (["cb", "cc", "da", "db"], 7),
            (["dd", "dc", "ad"], 4),
            (["dc", "da", "aa"], 5),
            (["dd", "dc"], 3),
            (["ac", "ab"], 4),
            (["bc", "cb", "dc", "bd"], 5),
            (["aa", "ba"], 3),
            (["aa", "bc", "bb"], 5),
            (["bd", "dc"], 3),
            (["ca", "cb", "bb", "ba"], 6),
            (["ac", "dd", "ba", "db"], 5),
            (["ac", "ca", "bd"], 5),
            (["da", "ba", "bb"], 5),
            (["dd", "ab"], 4),
            (["cb", "da"], 4),
            (["ad", "bc", "ba", "da"], 6),
            (["bd", "da", "cc", "ad"], 6),
            (["aa", "ab", "ac", "ad", "ba", "bb", "bc", "bd", "ca", "cb", "cc", "cd"], 15),
        ],
    )
    def test_shortest_superstring(self, words: list[str], expected: int):
        result = run_shortest_superstring(Solution, words)
        assert all(w in result for w in words)
        assert_shortest_superstring(result, expected)
