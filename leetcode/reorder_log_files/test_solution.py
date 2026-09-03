import pytest

from leetcode_py import logged_test

from .helpers import assert_reorder_log_files, run_reorder_log_files
from .solution import Solution


class TestReorderLogFiles:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "logs, expected",
        [
            (["a1 9 2 3 1", "g1 act car"], ["g1 act car", "a1 9 2 3 1"]),
            (["g1 act car", "a1 9 2 3 1"], ["g1 act car", "a1 9 2 3 1"]),
            (["b1 a"], ["b1 a"]),
            (["i1 0"], ["i1 0"]),
            (["a1 1", "b2 2"], ["a1 1", "b2 2"]),
            (["b2 2", "a1 1"], ["b2 2", "a1 1"]),
            (["d1 b a", "a1 a b"], ["a1 a b", "d1 b a"]),
            (["x1 c", "x2 b", "x3 a"], ["x3 a", "x2 b", "x1 c"]),
            (["a1 x", "a1 x"], ["a1 x", "a1 x"]),
            (["a1 ab", "a0 ab"], ["a0 ab", "a1 ab"]),
            (["t1 c b a", "t2 c b a", "t0 c b a"], ["t0 c b a", "t1 c b a", "t2 c b a"]),
            (["z9 zz yy", "y9 zz yy"], ["y9 zz yy", "z9 zz yy"]),
            (["m1 x", "m2 1", "m3 y", "m4 2"], ["m1 x", "m3 y", "m2 1", "m4 2"]),
            (["d1 5", "c1 b a", "d2 1", "a1 a"], ["a1 a", "c1 b a", "d1 5", "d2 1"]),
            (
                ["d1 8", "let1 art", "dig2 3", "let2 kit"],
                ["let1 art", "let2 kit", "d1 8", "dig2 3"],
            ),
            (
                ["a1 9", "g1 act car", "zo4 7", "ab1 dog"],
                ["g1 act car", "ab1 dog", "a1 9", "zo4 7"],
            ),
        ],
    )
    def test_reorder_log_files(self, logs: list[str], expected: list[str]):
        result = run_reorder_log_files(Solution, logs)
        assert_reorder_log_files(result, expected)
