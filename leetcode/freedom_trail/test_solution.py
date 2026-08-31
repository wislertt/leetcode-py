import pytest

from leetcode_py import logged_test

from .helpers import assert_find_rotate_steps, run_find_rotate_steps
from .solution import Solution


class TestFreedomTrail:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ring, key, expected",
        [
            ("godding", "gd", 4),
            ("godding", "godding", 13),
            ("a", "a", 1),
            ("ab", "b", 2),
            ("ab", "a", 1),
            ("abc", "abc", 5),
            ("abc", "cba", 6),
            ("edcba", "abcde", 10),
            ("xyzx", "xzyx", 8),
            ("aaaa", "aa", 2),
            ("abab", "baab", 7),
            ("x", "xxx", 3),
            ("knmop", "monk", 10),
            ("zxcvb", "vcxz", 9),
        ],
    )
    def test_find_rotate_steps(self, ring: str, key: str, expected: int):
        result = run_find_rotate_steps(Solution, ring, key)
        assert_find_rotate_steps(result, expected)
