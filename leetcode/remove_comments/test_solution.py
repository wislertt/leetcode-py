import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_comments, run_remove_comments
from .solution import Solution


class TestRemoveComments:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "source, expected",
        [
            (["g"], ["g"]),
            (["//x"], []),
            (["a//x"], ["a"]),
            (["/*c*/"], []),
            (["a/*c*/b"], ["ab"]),
            (["/*c", "*/"], []),
            (["a/*c", "d*/b"], ["ab"]),
            (["a/*comment", "line", "more_comment*/b"], ["ab"]),
            (["a/*/", "b*/c"], ["ac"]),
            (["x/*a*/y/*b*/z"], ["xyz"]),
            (["/*//*/k"], ["k"]),
            (["a//b/*c*/d"], ["a"]),
            (["/*", "a", "*/x", "y"], ["x", "y"]),
            (["a//*b*/c"], ["a"]),
            (["/*a//*/b"], ["b"]),
            (["/*a*/", "/*b*/x"], ["x"]),
            (["a/*b*/", "c"], ["a", "c"]),
            (["{ ", "  // v ", "int a;"], ["{ ", "  ", "int a;"]),
            (["/*Test program */", "int main()"], ["int main()"]),
            (["/* t", "   m */x", "}"], ["x", "}"]),
        ],
    )
    def test_remove_comments(self, source: list[str], expected: list[str]):
        result = run_remove_comments(Solution, source)
        assert_remove_comments(result, expected)
