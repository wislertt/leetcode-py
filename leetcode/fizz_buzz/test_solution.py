import pytest

from leetcode_py import logged_test

from .helpers import assert_fizz_buzz, run_fizz_buzz
from .solution import Solution


class TestFizzBuzz:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, ["1"]),
            (2, ["1", "2"]),
            (3, ["1", "2", "Fizz"]),
            (4, ["1", "2", "Fizz", "4"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (6, ["1", "2", "Fizz", "4", "Buzz", "Fizz"]),
            (7, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]),
            (8, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8"]),
            (9, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz"]),
            (10, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]),
            (11, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11"]),
            (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
            ),
        ],
    )
    def test_fizz_buzz(self, n: int, expected: list[str]):
        result = run_fizz_buzz(Solution, n)
        assert_fizz_buzz(result, expected)
