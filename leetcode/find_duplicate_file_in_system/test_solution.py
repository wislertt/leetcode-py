import pytest

from leetcode_py import logged_test

from .helpers import assert_find_duplicate, run_find_duplicate
from .solution import Solution


class TestFindDuplicateFileInSystem:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "paths, expected",
        [
            (
                [
                    "root/a 1.txt(abcd) 2.txt(efgh)",
                    "root/c 3.txt(abcd)",
                    "root/c/d 4.txt(efgh)",
                    "root 4.txt(efgh)",
                ],
                [
                    ["root/4.txt", "root/a/2.txt", "root/c/d/4.txt"],
                    ["root/a/1.txt", "root/c/3.txt"],
                ],
            ),
            (
                ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"],
                [["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt"]],
            ),
            (["a 1.txt(x)"], []),
            (["r/a 1.txt(x)", "r/b 1.txt(x)"], [["r/a/1.txt", "r/b/1.txt"]]),
            (["r/a 1.txt(x)", "r/b 1.txt(y)"], []),
            (["d 1.txt(z)", "d2 1.txt(z)", "d3 1.txt(z)"], [["d/1.txt", "d2/1.txt", "d3/1.txt"]]),
            (["r 1.txt(w) 2.txt(w)"], [["r/1.txt", "r/2.txt"]]),
            (["r 1.txt(w) 2.txt(v)"], []),
            (["r 1.txt(a/b)", "q 2.txt(a/b)"], [["q/2.txt", "r/1.txt"]]),
            (["x f.txt(1.2.3)", "y g.txt(1.2.3)"], [["x/f.txt", "y/g.txt"]]),
            (["root/x/y 1.txt(c)", "root/z 1.txt(c)"], [["root/x/y/1.txt", "root/z/1.txt"]]),
            (
                ["a 1.txt(p) 2.txt(q)", "b 1.txt(q) 2.txt(p)"],
                [["a/1.txt", "b/2.txt"], ["a/2.txt", "b/1.txt"]],
            ),
            (["a v1.2.txt(k)", "b v1.2.txt(k)"], [["a/v1.2.txt", "b/v1.2.txt"]]),
            (["a 1.txt()", "b 1.txt()"], [["a/1.txt", "b/1.txt"]]),
            (
                ["a 1.txt(m) 2.txt(n) 3.txt(m)", "b 1.txt(n) 2.txt(m)"],
                [["a/1.txt", "a/3.txt", "b/2.txt"], ["a/2.txt", "b/1.txt"]],
            ),
            (["root 1.txt(a)"], []),
        ],
    )
    def test_find_duplicate(self, paths: list[str], expected: list[list[str]]):
        result = run_find_duplicate(Solution, paths)
        assert_find_duplicate(result, expected)
