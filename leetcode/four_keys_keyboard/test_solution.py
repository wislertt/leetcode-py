import pytest

from leetcode_py import logged_test

from .helpers import assert_max_a, run_max_a
from .solution import Solution


class TestFourKeysKeyboard:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 9),
            (8, 12),
            (9, 16),
            (10, 20),
            (11, 27),
            (12, 36),
            (13, 48),
            (14, 64),
            (15, 81),
            (16, 108),
            (17, 144),
            (18, 192),
            (19, 256),
            (20, 324),
            (21, 432),
            (22, 576),
            (23, 768),
            (24, 1024),
            (25, 1296),
            (30, 5184),
            (35, 20736),
            (40, 82944),
            (45, 331776),
            (50, 1327104),
        ],
    )
    def test_max_a(self, n: int, expected: int):
        result = run_max_a(Solution, n)
        assert_max_a(result, expected)
