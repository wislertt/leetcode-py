import pytest

from leetcode_py import logged_test

from .helpers import assert_image_smoother, run_image_smoother
from .solution import Solution


class TestImageSmoother:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "img, expected",
        [
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
            (
                [[100, 200, 100], [200, 50, 200], [100, 200, 100]],
                [[137, 141, 137], [141, 138, 141], [137, 141, 137]],
            ),
            ([[5]], [[5]]),
            ([[2, 3]], [[2, 2]]),
            ([[1, 2, 3]], [[1, 2, 2]]),
            ([[1], [2], [3]], [[1], [2], [2]]),
            ([[7, 7], [7, 7]], [[7, 7], [7, 7]]),
            ([[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]),
            (
                [[255, 255, 255], [255, 255, 255], [255, 255, 255]],
                [[255, 255, 255], [255, 255, 255], [255, 255, 255]],
            ),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[3, 3, 4], [4, 5, 5], [6, 6, 7]]),
            ([[10, 20, 30, 40]], [[15, 20, 30, 35]]),
            ([[10], [20], [30], [40]], [[15], [20], [30], [35]]),
            (
                [[255, 0, 255], [0, 255, 0], [255, 0, 255]],
                [[127, 127, 127], [127, 141, 127], [127, 127, 127]],
            ),
            ([[1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [1, 1, 1, 1]]),
        ],
    )
    def test_image_smoother(self, img: list[list[int]], expected: list[list[int]]):
        result = run_image_smoother(Solution, img)
        assert_image_smoother(result, expected)
