import pytest

from leetcode_py import logged_test

from .helpers import assert_min_stickers, run_min_stickers
from .solution import Solution


class TestStickersToSpellWord:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stickers, target, expected",
        [
            (["with", "example", "science"], "thehat", 3),
            (["notice", "possible"], "basicbasic", -1),
            (["a"], "a", 1),
            (["a"], "aaaaa", 5),
            (["ab"], "ba", 1),
            (["ab", "bc"], "abc", 2),
            (["these", "guess", "about", "garden", "him"], "atomher", 3),
            (["fly", "me", "grass", "planet", "enter"], "plantenemy", 4),
            (["control", "heart"], "heartcontrol", 2),
            (["summer", "winter", "autumn", "spring"], "summertime", 3),
            (["aaa", "bbb", "ccc"], "abcabcabc", 3),
            (["x"], "y", -1),
            (["and", "two", "their", "playing"], "angling", 2),
        ],
    )
    def test_min_stickers(self, stickers: list[str], target: str, expected: int):
        result = run_min_stickers(Solution, stickers, target)
        assert_min_stickers(result, expected)
