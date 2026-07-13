import pytest

from leetcode_py import logged_test

from .helpers import assert_lemonade_change, run_lemonade_change
from .solution import Solution


class TestLemonadeChange:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "bills, expected",
        [
            ([5, 5, 5, 10, 20], True),
            ([5, 5, 10, 10, 20], False),
            ([5, 5, 5, 5, 5], True),
            ([10], False),
            ([5], True),
            ([5, 10], True),
            ([5, 10, 5], True),
            ([5, 20], False),
            ([5, 5, 5, 5, 20, 20], False),
            ([5, 5, 10, 20], True),
            ([5, 5, 5, 10, 5, 20], True),
            ([20], False),
            ([5, 5, 5, 5, 5, 5, 10, 10, 10, 20, 20, 20], True),
            ([5, 10, 5, 20], True),
            ([5, 5, 10, 20, 5, 5, 10, 20], True),
            ([5, 5, 5, 5, 5, 10, 5, 10, 20, 20], True),
        ],
    )
    def test_lemonade_change(self, bills: list[int], expected: bool):
        result = run_lemonade_change(Solution, bills)
        assert_lemonade_change(result, expected)
