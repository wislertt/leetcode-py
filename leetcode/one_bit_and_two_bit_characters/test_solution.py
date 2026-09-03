import pytest

from leetcode_py import logged_test

from .helpers import assert_is_one_bit_character, run_is_one_bit_character
from .solution import Solution


class TestOneBitAndTwoBitCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "bits, expected",
        [
            ([1, 0, 0], True),
            ([1, 1, 1, 0], False),
            ([0], True),
            ([1, 0], False),
            ([0, 0], True),
            ([1, 1, 0], True),
            ([0, 1, 0], False),
            ([1, 0, 1, 0], False),
            ([1, 1, 0, 0], True),
            ([0, 0, 0, 0], True),
            ([1, 1, 1, 1, 0], True),
            ([1, 0, 1, 1, 0], True),
            ([1, 1, 0, 1, 0], False),
            ([0, 1, 1, 1, 0], False),
            ([1, 1, 1, 0, 1, 0], False),
            ([0, 1, 0, 1, 1, 0], True),
            ([0, 0, 1, 0], False),
            ([1, 1, 0, 1, 1, 0, 1, 1, 1, 0], False),
            ([0, 0, 1, 0, 0, 0, 0, 0, 0], True),
            ([1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0], True),
        ],
    )
    def test_is_one_bit_character(self, bits: list[int], expected: bool):
        result = run_is_one_bit_character(Solution, bits)
        assert_is_one_bit_character(result, expected)
