import pytest

from leetcode_py import logged_test

from .helpers import assert_min_deletions, run_min_deletions
from .solution import Solution


class TestMinimumDeletionsToMakeCharacterFrequenciesUnique:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aab", 0),
            ("aaabbbcc", 2),
            ("ceabaacb", 2),
            ("abcde", 4),
            ("a", 0),
            ("bb", 0),
            ("aabbcc", 3),
            ("abcabc", 3),
            ("aabb", 1),
            ("aaabbb", 1),
            ("abbcccdddd", 0),
            ("abcdefghij", 9),
            ("aabbccdd", 5),
            ("zzzzyyyyxxxx", 3),
            ("oinclabovhnphne", 9),
            ("hztiqq", 3),
            ("zlzt", 1),
            ("bddcqxunzpeulhnsbrgjvata", 21),
            ("qbl", 2),
            ("pwjewoext", 6),
            ("njlqhsgxlkni", 9),
            ("bpivowjyktgfdyddnrw", 13),
        ],
    )
    def test_min_deletions(self, s: str, expected: int):
        result = run_min_deletions(Solution, s)
        assert_min_deletions(result, expected)
