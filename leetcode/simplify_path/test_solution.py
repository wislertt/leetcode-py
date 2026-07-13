import pytest

from leetcode_py import logged_test

from .helpers import assert_simplify_path, run_simplify_path
from .solution import Solution


class TestTestSimplifyPath:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, path, expected",
        [
            (Solution, "/home/", "/home"),
            (Solution, "/home//foo/", "/home/foo"),
            (Solution, "/home/user/Documents/../Pictures", "/home/user/Pictures"),
            (Solution, "/../", "/"),
            (Solution, "/.../a/../b/c/../d/./", "/.../b/d"),
            (Solution, "/", "/"),
            (Solution, "/.", "/"),
            (Solution, "/..", "/"),
            (Solution, "/./", "/"),
            (Solution, "/a/./b/../../../c/", "/c"),
            (Solution, "/a//b////c/d//././/..", "/a/b/c"),
            (Solution, "/.../", "/..."),
            (Solution, "/....", "/...."),
            (Solution, "/../..", "/"),
            (Solution, "/a/b/c", "/a/b/c"),
            (Solution, "/../a", "/a"),
            (Solution, "/a/..", "/"),
            (Solution, "/home/foo/./bar/", "/home/foo/bar"),
        ],
    )
    def test_simplify_path(self, solution_class, path: str, expected: str):
        result = run_simplify_path(solution_class, path)
        assert_simplify_path(result, expected)
