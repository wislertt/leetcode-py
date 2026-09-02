import pytest

from leetcode_py import logged_test

from .helpers import assert_detect_capital_use, run_detect_capital_use
from .solution import Solution


class TestDetectCapital:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("USA", True),
            ("FlaG", False),
            ("leetcode", True),
            ("Google", True),
            ("A", True),
            ("a", True),
            ("AB", True),
            ("Ab", True),
            ("aB", False),
            ("ABC", True),
            ("aBC", False),
            ("ABc", False),
            ("Leetcode", True),
            ("leetcodE", False),
            ("AaA", False),
            ("g", True),
            ("ALLCAPS", True),
            ("alllower", True),
            ("Capitalized", True),
            ("mIxEd", False),
        ],
    )
    def test_detect_capital_use(self, word: str, expected: bool):
        result = run_detect_capital_use(Solution, word)
        assert_detect_capital_use(result, expected)
