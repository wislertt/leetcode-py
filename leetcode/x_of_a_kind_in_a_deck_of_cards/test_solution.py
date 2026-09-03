import pytest

from leetcode_py import logged_test

from .helpers import assert_has_group_size_x, run_has_group_size_x
from .solution import Solution


class TestXOfAKindInADeckOfCards:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "deck, expected",
        [
            ([1, 2, 3, 4, 4, 3, 2, 1], True),
            ([1, 1, 1, 2, 2, 2, 3, 3], False),
            ([1], False),
            ([1, 1], True),
            ([1, 2], False),
            ([0, 0, 0, 0], True),
            ([0, 0, 0], True),
            ([1, 1, 1, 1, 1, 1], True),
            ([1, 1, 1, 1, 1], True),
            ([2, 2, 2, 3], False),
            ([1, 1, 2, 2, 3, 3], True),
            ([1, 1, 1, 2, 2, 2, 3, 3, 3], True),
            ([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], True),
            ([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3], False),
            ([1, 1, 2, 2, 2, 2], True),
            ([6, 6, 6, 6, 6, 6, 6, 6, 6, 6], True),
            ([6, 6, 6, 6, 6, 6, 6, 6, 6], True),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),
            ([2], False),
            ([7, 7, 7], True),
            ([6, 6, 0, 5, 6, 5], False),
            ([9, 9, 9, 9, 9, 6, 6, 6, 4], False),
            ([7, 1, 1, 7, 7, 7, 1, 7], False),
            ([2, 2, 2, 2, 4, 2, 2, 2, 4, 2], True),
        ],
    )
    def test_has_group_size_x(self, deck: list[int], expected: bool):
        result = run_has_group_size_x(Solution, deck)
        assert_has_group_size_x(result, expected)
