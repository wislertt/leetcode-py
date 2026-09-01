import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_stars, run_remove_stars
from .solution import Solution


class TestRemovingStarsFromAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("leet**cod*e", "lecoe"),
            ("erase*****", ""),
            ("a", "a"),
            ("a*", ""),
            ("aa*", "a"),
            ("ab*", "a"),
            ("abc*", "ab"),
            ("abc***", ""),
            ("ab**c", "c"),
            ("a*b*c*d*", ""),
            ("z*z*z*", ""),
            ("abc*de**f*", "ab"),
            ("leet*code", "leecode"),
            ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa******************************b", "b"),
        ],
    )
    def test_remove_stars(self, s: str, expected: str):
        result = run_remove_stars(Solution, s)
        assert_remove_stars(result, expected)
