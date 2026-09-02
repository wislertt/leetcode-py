import pytest

from leetcode_py import logged_test

from .helpers import assert_max_number_of_balloons, run_max_number_of_balloons
from .solution import Solution


class TestMaximumNumberOfBalloonsTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("nlaebolko", 1),
            ("loonbalxballpoon", 2),
            ("leetcode", 0),
            ("balloon", 1),
            ("balloonballoon", 2),
            ("balon", 0),
            ("a", 0),
            ("b", 0),
            ("l", 0),
            ("o", 0),
            ("n", 0),
            ("bnl", 0),
            ("nooln", 0),
            ("balllllllllllloooooooooooon", 1),
            ("abcabcabc", 0),
            ("balloonlo", 1),
        ],
    )
    def test_max_number_of_balloons(self, text: str, expected: int):
        result = run_max_number_of_balloons(Solution, text)
        assert_max_number_of_balloons(result, expected)
