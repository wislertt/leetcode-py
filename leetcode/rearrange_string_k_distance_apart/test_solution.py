import pytest

from leetcode_py import logged_test

from .helpers import assert_rearrange_string, run_rearrange_string
from .solution import Solution


class TestRearrangeStringKDistanceApart:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k",
        [
            ("aabbcc", 3),
            ("aaabc", 3),
            ("aaadbbcc", 2),
            ("a", 0),
            ("a", 1),
            ("aa", 2),
            ("aa", 1),
            ("aabb", 2),
            ("aaabbc", 3),
            ("aabbcc", 2),
            ("abcabc", 3),
            ("aaadbbcc", 3),
            ("aaaa", 4),
            ("abb", 2),
            ("abcbaca", 2),
            ("abcbaca", 3),
            ("zzz", 1),
            ("aabbccdd", 4),
            ("abcabc", 0),
            ("aabb", 0),
        ],
    )
    def test_rearrange_string(self, s: str, k: int):
        result = run_rearrange_string(Solution, s, k)
        assert_rearrange_string(result, s, k)
