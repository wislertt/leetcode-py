import pytest

from leetcode_py import logged_test

from .helpers import assert_can_reach, run_can_reach
from .solution import Solution


class TestTestJumpGameVII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, min_jump, max_jump, expected",
        [
            ("011010", 2, 3, True),
            ("01101110", 2, 3, False),
            ("00", 1, 1, True),
            ("01", 1, 1, False),
            ("000", 1, 2, True),
            ("00000", 2, 3, True),
            ("011110", 2, 5, True),
            ("011110", 3, 4, False),
            ("000000", 1, 1, True),
            ("010", 2, 2, True),
            ("010", 1, 2, True),
            ("0110", 2, 2, False),
            ("0000", 3, 3, True),
            ("0001000", 1, 3, True),
            ("001100", 2, 3, False),
        ],
    )
    def test_can_reach(self, s: str, min_jump: int, max_jump: int, expected: bool):
        result = run_can_reach(Solution, s, min_jump, max_jump)
        assert_can_reach(result, expected)
