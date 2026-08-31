import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_patterns, run_number_of_patterns
from .solution import Solution


class TestAndroidUnlockPatterns:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, expected",
        [
            (1, 1, 9),
            (1, 2, 65),
            (2, 2, 56),
            (1, 3, 385),
            (3, 3, 320),
            (1, 9, 389497),
            (9, 9, 140704),
            (2, 3, 376),
            (4, 4, 1624),
            (8, 9, 281408),
            (5, 5, 7152),
            (6, 6, 26016),
            (7, 7, 72912),
            (1, 4, 2009),
            (2, 9, 389488),
        ],
    )
    def test_number_of_patterns(self, m: int, n: int, expected: int):
        result = run_number_of_patterns(Solution, m, n)
        assert_number_of_patterns(result, expected)
