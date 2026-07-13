import pytest

from leetcode_py import logged_test

from .helpers import assert_backspace_compare, run_backspace_compare
from .solution import Solution


class TestBackspaceStringCompare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("ab#c", "ad#c", True),
            ("ab##", "c#d#", True),
            ("a#c", "b", False),
            ("a", "a", True),
            ("#", "#", True),
            ("a#", "", True),
            ("a#b", "b", True),
            ("###", "", True),
            ("a##c", "#a#c", True),
            ("xywrrmp", "xywrrmu#p", True),
            ("c##vnvr", "vnvr", True),
            ("nzp#o", "b#nzp#o", True),
            ("abc", "abc", True),
            ("a", "b", False),
            ("ab#c", "ad#d", False),
        ],
    )
    def test_backspace_compare(self, s: str, t: str, expected: bool):
        result = run_backspace_compare(Solution, s, t)
        assert_backspace_compare(result, expected)
