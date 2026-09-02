import pytest

from leetcode_py import logged_test

from .helpers import assert_find_complement, run_find_complement
from .solution import Solution


class TestNumberComplement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (1, 0),
            (2, 1),
            (3, 0),
            (4, 3),
            (5, 2),
            (6, 1),
            (7, 0),
            (8, 7),
            (10, 5),
            (100, 27),
            (999, 24),
            (1000, 23),
            (12345, 4038),
            (65535, 0),
            (65536, 65535),
            (1073741824, 1073741823),
            (1073741823, 0),
            (2147483647, 0),
            (2147483646, 1),
            (536870912, 536870911),
            (4681, 3510),
            (26, 5),
        ],
    )
    def test_find_complement(self, num: int, expected: int):
        result = run_find_complement(Solution, num)
        assert_find_complement(result, expected)
