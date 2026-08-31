import pytest

from leetcode_py import logged_test

from .helpers import assert_frequency_sort, run_frequency_sort
from .solution import Solution


class TestSortCharactersByFrequency:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("tree", "eetr"),
            ("cccaaa", "aaaccc"),
            ("Aabb", "bbAa"),
            ("a", "a"),
            ("aa", "aa"),
            ("ab", "ab"),
            ("ba", "ab"),
            ("aaabbb", "bbbaaa"),
            ("abcabc", "aabbcc"),
            ("112233", "332211"),
            ("mississippi", "iiiissssppm"),
            ("aabbbcccc", "ccccbbbaa"),
            ("2a55bbb2222", "22222bbb55a"),
            ("eded", "eedd"),
        ],
    )
    def test_frequency_sort(self, s: str, expected: str):
        result = run_frequency_sort(Solution, s)
        assert_frequency_sort(result, expected)
