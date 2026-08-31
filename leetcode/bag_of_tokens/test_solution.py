import pytest

from leetcode_py import logged_test

from .helpers import assert_bag_of_tokens_score, run_bag_of_tokens_score
from .solution import Solution


class TestBagOfTokens:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tokens, power, expected",
        [
            ([100], 50, 0),
            ([200, 100], 150, 1),
            ([100, 200, 300, 400], 200, 2),
            ([], 100, 0),
            ([], 0, 0),
            ([0], 0, 1),
            ([50], 50, 1),
            ([50], 49, 0),
            ([1, 2], 2, 1),
            ([1, 2, 3], 3, 2),
            ([100, 200, 300, 400], 100, 1),
            ([71, 55, 82], 50, 0),
            ([26], 51, 1),
            ([24, 30], 24, 1),
            ([25, 76, 24], 50, 2),
        ],
    )
    def test_bag_of_tokens_score(self, tokens: list[int], power: int, expected: int):
        result = run_bag_of_tokens_score(Solution, tokens, power)
        assert_bag_of_tokens_score(result, expected)
