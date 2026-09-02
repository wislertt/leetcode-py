import pytest

from leetcode_py import logged_test

from .helpers import assert_gray_code, run_gray_code
from .solution import Solution


class TestGrayCode:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected_size",
        [
            (1, 2),
            (2, 4),
            (3, 8),
            (4, 16),
            (5, 32),
            (6, 64),
            (7, 128),
            (8, 256),
            (9, 512),
            (10, 1024),
            (11, 2048),
            (12, 4096),
            (13, 8192),
            (14, 16384),
            (15, 32768),
            (16, 65536),
        ],
    )
    def test_gray_code(self, n: int, expected_size: int):
        result = run_gray_code(Solution, n)
        assert_gray_code(result, expected_size)
