import pytest

from leetcode_py import logged_test

from .helpers import assert_rand10, run_rand10
from .solution import Solution


class TestImplementRand10UsingRand7:
    @logged_test
    @pytest.mark.parametrize(
        "seed, n, expected",
        [
            (0, 1, 1),
            (1, 2, 2),
            (2, 3, 3),
            (3, 5, 5),
            (4, 7, 7),
            (5, 10, 10),
            (6, 13, 13),
            (7, 20, 20),
            (8, 25, 25),
            (9, 30, 30),
            (10, 40, 40),
            (11, 50, 50),
            (12, 75, 75),
            (13, 100, 100),
            (14, 150, 150),
            (15, 200, 200),
            (42, 300, 300),
            (7, 1, 1),
            (99, 100000, 100000),
        ],
    )
    def test_rand10(self, seed: int, n: int, expected: int):
        result = run_rand10(Solution, seed, n)
        assert_rand10(result, expected)
