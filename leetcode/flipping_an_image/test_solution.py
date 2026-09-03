import pytest

from leetcode_py import logged_test

from .helpers import assert_flip_and_invert_image, run_flip_and_invert_image
from .solution import Solution


class TestFlippingAnImage:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "image, expected",
        [
            ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
            ([[0]], [[1]]),
            ([[1]], [[0]]),
            ([[0, 0], [0, 0]], [[1, 1], [1, 1]]),
            ([[1, 1], [1, 1]], [[0, 0], [0, 0]]),
            ([[0, 1], [1, 0]], [[0, 1], [1, 0]]),
            ([[0, 1], [1, 1]], [[0, 1], [0, 0]]),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], [[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
            ([[1, 1, 0], [0, 1, 1], [1, 0, 0]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]),
            ([[0, 1, 1], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 1, 0], [1, 0, 1]]),
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 0, 1], [0, 1, 1]]),
            ([[1, 0, 1], [1, 0, 0], [1, 1, 0]], [[0, 1, 0], [1, 1, 0], [1, 0, 0]]),
            ([[1, 0, 1], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [0, 1, 1], [1, 1, 0]]),
            ([[0, 1, 1], [0, 0, 0], [0, 1, 0]], [[0, 0, 1], [1, 1, 1], [1, 0, 1]]),
            ([[1, 1, 0], [1, 1, 0], [0, 1, 0]], [[1, 0, 0], [1, 0, 0], [1, 0, 1]]),
        ],
    )
    def test_flip_and_invert_image(self, image: list[list[int]], expected: list[list[int]]):
        result = run_flip_and_invert_image(Solution, image)
        assert_flip_and_invert_image(result, expected)
