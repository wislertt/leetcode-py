import pytest

from leetcode_py import logged_test

from .helpers import assert_validate_stack_sequences, run_validate_stack_sequences
from .solution import Solution


class TestValidateStackSequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "pushed, popped, expected",
        [
            ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
            ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
            ([1], [1], True),
            ([1, 2], [1, 2], True),
            ([1, 2], [2, 1], True),
            ([1, 2, 3], [3, 2, 1], True),
            ([1, 2, 3], [3, 1, 2], False),
            ([1, 2, 3], [1, 3, 2], True),
            ([2, 1, 0], [1, 2, 0], True),
            ([0, 1, 2, 3], [0, 3, 2, 1], True),
            ([1, 0, 3, 2], [0, 1, 2, 3], True),
            ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4], True),
            ([1, 2, 3, 4], [2, 1, 4, 3], True),
            ([1, 2, 3, 4], [4, 1, 2, 3], False),
            ([10, 20, 30, 40], [30, 40, 20, 10], True),
        ],
    )
    def test_validate_stack_sequences(self, pushed: list[int], popped: list[int], expected: bool):
        result = run_validate_stack_sequences(Solution, pushed, popped)
        assert_validate_stack_sequences(result, expected)
