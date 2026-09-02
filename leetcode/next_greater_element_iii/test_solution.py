import pytest

from leetcode_py import logged_test

from .helpers import assert_next_greater_element, run_next_greater_element
from .solution import Solution


class TestNextGreaterElementIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (12, 21),
            (21, -1),
            (1, -1),
            (11, -1),
            (9, -1),
            (10, -1),
            (111, -1),
            (1234, 1243),
            (4321, -1),
            (12345678, 12345687),
            (2147483647, -1),
            (2147483476, 2147483647),
            (1999999999, -1),
            (230241, 230412),
            (12443322, 13222344),
            (534976, 536479),
            (1234567, 1234576),
            (11122, 11212),
            (218765, 251678),
            (987654321, -1),
            (1200000, 2000001),
            (13531, 15133),
        ],
    )
    def test_next_greater_element(self, n: int, expected: int):
        result = run_next_greater_element(Solution, n)
        assert_next_greater_element(result, expected)
