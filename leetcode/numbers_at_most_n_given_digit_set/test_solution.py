import pytest

from leetcode_py import logged_test

from .helpers import assert_at_most_n_given_digit_set, run_at_most_n_given_digit_set
from .solution import Solution


class TestNumbersAtMostNGivenDigitSet:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "digits, n, expected",
        [
            (["1", "3", "5", "7"], 100, 20),
            (["1", "4", "9"], 1000000000, 29523),
            (["7"], 8, 1),
            (["1"], 1, 1),
            (["1"], 1000000000, 9),
            (["9"], 1, 0),
            (["7"], 5, 0),
            (["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1000000000, 435848049),
            (["3", "5"], 40, 4),
            (["2"], 222, 3),
            (["1", "2"], 25, 6),
            (["5", "6", "7"], 600, 21),
            (["8", "9"], 100, 6),
            (["1", "3", "5"], 1000, 39),
            (["4"], 4000, 3),
            (["2", "4", "6", "8"], 999, 84),
            (["1", "2", "5", "7", "8"], 2786, 378),
            (["1", "2", "3", "4", "5", "6", "7", "8", "9"], 2492, 1865),
            (["2", "3", "4", "5", "7"], 1254, 155),
            (["1", "4", "9"], 2036, 66),
        ],
    )
    def test_at_most_n_given_digit_set(self, digits: list[str], n: int, expected: int):
        result = run_at_most_n_given_digit_set(Solution, digits, n)
        assert_at_most_n_given_digit_set(result, expected)
