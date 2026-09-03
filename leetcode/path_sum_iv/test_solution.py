import pytest

from leetcode_py import logged_test

from .helpers import assert_path_sum, run_path_sum
from .solution import Solution


class TestPathSumIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([113, 215, 221], 12),
            ([113, 221], 4),
            ([113], 3),
            ([119], 9),
            ([113, 214], 7),
            ([111, 212, 221, 314, 328], 20),
            ([113, 215, 221, 315, 328], 33),
            ([113, 214, 221, 315], 16),
            ([112, 213, 224, 316, 327, 335, 338], 37),
            ([117, 211, 224, 312, 320, 331, 347, 418, 427, 436, 445, 455, 464, 470, 482], 133),
            ([118, 218, 223, 318, 327], 58),
            ([117, 213, 222, 338, 348, 461, 473, 487], 72),
            ([111, 210, 224, 314, 325, 341, 429], 26),
            ([113, 225], 8),
            ([116, 218, 229, 319, 320, 334, 346, 433, 446, 451, 477, 487], 136),
            ([116, 211, 221, 327, 330, 342, 461], 31),
            ([113, 219, 312, 321, 416, 422, 431, 445], 68),
        ],
    )
    def test_path_sum(self, nums: list[int], expected: int):
        result = run_path_sum(Solution, nums)
        assert_path_sum(result, expected)
