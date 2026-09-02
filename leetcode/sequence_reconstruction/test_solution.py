import pytest

from leetcode_py import logged_test

from .helpers import assert_sequence_reconstruction, run_sequence_reconstruction
from .solution import Solution


class TestSequenceReconstruction:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, sequences, expected",
        [
            ([1, 2, 3], [[1, 2], [1, 3]], False),
            ([1, 2, 3], [[1, 2]], False),
            ([1, 2, 3], [[1, 2], [1, 3], [2, 3]], True),
            ([1], [[1]], True),
            ([2, 1], [[2, 1]], True),
            ([4, 1, 5, 2, 3], [[4, 1], [1, 5], [5, 2], [2, 3], [4, 1, 5, 2, 3]], True),
            ([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4], [1, 2, 3, 4]], True),
            ([1, 2, 3], [[1, 2], [2, 3], [1, 3], [1, 2, 3]], True),
            ([2, 1, 3], [[2, 1], [1, 3]], True),
            ([1, 3, 2], [[1, 3], [3, 2], [1, 2]], True),
            ([1, 2, 3, 4], [[1, 3], [2, 4]], False),
            ([3, 1, 2], [[1], [3, 1], [2]], False),
        ],
    )
    def test_sequence_reconstruction(
        self, nums: list[int], sequences: list[list[int]], expected: bool
    ):
        result = run_sequence_reconstruction(Solution, nums, sequences)
        assert_sequence_reconstruction(result, expected)
