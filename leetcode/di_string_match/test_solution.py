import pytest

from leetcode_py import logged_test

from .helpers import assert_di_string_match, run_di_string_match
from .solution import Solution


class TestDIStringMatch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("IDID", [0, 4, 1, 3, 2]),
            ("III", [0, 1, 2, 3]),
            ("DDI", [3, 2, 0, 1]),
            ("I", [0, 1]),
            ("D", [1, 0]),
            ("II", [0, 1, 2]),
            ("DD", [2, 1, 0]),
            ("ID", [0, 2, 1]),
            ("DI", [2, 0, 1]),
            ("IDI", [0, 3, 1, 2]),
            ("DID", [3, 0, 2, 1]),
            ("IDIDID", [0, 6, 1, 5, 2, 4, 3]),
            ("DDDD", [4, 3, 2, 1, 0]),
            ("IIII", [0, 1, 2, 3, 4]),
            ("IDIDDI", [0, 6, 1, 5, 4, 2, 3]),
            ("DIIDID", [6, 0, 1, 5, 2, 4, 3]),
        ],
    )
    def test_di_string_match(self, s: str, expected: list[int]):
        result = run_di_string_match(Solution, s)
        assert_di_string_match(result, expected, s)
