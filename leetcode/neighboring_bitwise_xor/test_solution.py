import pytest

from leetcode_py import logged_test

from .helpers import assert_does_valid_array_exist, run_does_valid_array_exist
from .solution import Solution


class TestNeighboringBitwiseXor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "derived, expected",
        [
            ([1, 1, 0], True),
            ([1, 1], True),
            ([1, 0], False),
            ([0], True),
            ([1], False),
            ([0, 0], True),
            ([0, 1], False),
            ([1, 0, 1], True),
            ([0, 0, 0], True),
            ([1, 1, 1, 1], True),
            ([1, 1, 1], False),
            ([0, 1, 0, 1], True),
            ([1, 0, 0, 1], True),
            ([0, 1, 1, 0, 0], True),
            ([1, 0, 0, 0, 1, 0], True),
            ([0, 1, 1, 0], True),
            ([1, 1, 1, 1, 0, 0, 0], True),
            ([1], False),
            ([1, 1, 0, 1, 1, 0], True),
            ([1, 0, 0, 0, 0, 1], True),
        ],
    )
    def test_does_valid_array_exist(self, derived: list[int], expected: bool):
        result = run_does_valid_array_exist(Solution, derived)
        assert_does_valid_array_exist(result, expected)
