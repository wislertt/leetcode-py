import pytest

from leetcode_py import logged_test

from .helpers import assert_orderly_queue, run_orderly_queue
from .solution import Solution


class TestOrderlyQueue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("cba", 1, "acb"),
            ("baaca", 3, "aaabc"),
            ("a", 1, "a"),
            ("ab", 1, "ab"),
            ("ba", 1, "ab"),
            ("ba", 2, "ab"),
            ("cab", 2, "abc"),
            ("aaab", 1, "aaab"),
            ("bbaa", 1, "aabb"),
            ("dcba", 4, "abcd"),
            ("dcba", 1, "adcb"),
            ("zzza", 2, "azzz"),
            ("xyx", 3, "xxy"),
            ("kuus", 1, "kuus"),
            ("gwk", 1, "gwk"),
            ("edcba", 1, "aedcb"),
            ("abcabc", 1, "abcabc"),
            ("zyxwvu", 2, "uvwxyz"),
            ("aabbcc", 5, "aabbcc"),
            ("kkkk", 1, "kkkk"),
            ("bxcdaweafq", 1, "afqbxcdawe"),
            ("bxcdaweafq", 2, "aabcdefqwx"),
            ("qwertyuiopasdfghjklz", 1, "asdfghjklzqwertyuiop"),
            ("mnoapqrstuvwbyzabcxd", 2, "aabbcdmnopqrstuvwxyz"),
        ],
    )
    def test_orderly_queue(self, s: str, k: int, expected: str):
        result = run_orderly_queue(Solution, s, k)
        assert_orderly_queue(result, expected)
