import pytest

from leetcode_py import logged_test

from .helpers import assert_replace_words, run_replace_words
from .solution import Solution


class TestReplaceWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "dictionary, sentence, expected",
        [
            (
                ["cat", "bat", "rat"],
                "the cattle was rattled by the battery",
                "the cat was rat by the bat",
            ),
            (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs", "a a b c"),
            (["cattle"], "cattle", "cattle"),
            (["cattle"], "cat dog", "cat dog"),
            (["cat", "cattle"], "cattle dog", "cat dog"),
            (["ca", "cat"], "cat cattle", "ca ca"),
            (["a"], "apple banana", "a banana"),
            (["an", "b"], "ant banana cat", "an b cat"),
            (["rat", "ra"], "rat rattly ratatat", "ra ra ra"),
            (["help"], "help helpful helping", "help help help"),
            (["s"], "cats and dogs", "cats and dogs"),
            (["x"], "abc def ghi", "abc def ghi"),
            (["ab", "abc"], "abcabc abc ab", "ab ab ab"),
            (["z"], "zoo z", "z z"),
            (["sk", "dn", "pzs", "ysdc"], "ysdc ysdcki i", "ysdc ysdc i"),
            (["j", "f", "iyg", "dup"], "iyg cg jpltiy dup", "iyg cg j dup"),
            (["zzb", "qc", "wl", "gvs"], "rp wllhx", "rp wl"),
            (["udyl", "vad", "y", "uv"], "vadvanbd udylw udyl", "vad udyl udyl"),
            (["lqn", "lf", "cb", "zq"], "zqxajla lf lfcxrkst wrqkcogn", "zq lf lf wrqkcogn"),
            (["g", "nrnm", "scmf", "w"], "ooqg z dzy scmff scmfko xg", "ooqg z dzy scmf scmf xg"),
        ],
    )
    def test_replace_words(self, dictionary: list[str], sentence: str, expected: str):
        result = run_replace_words(Solution, dictionary, sentence)
        assert_replace_words(result, expected)
