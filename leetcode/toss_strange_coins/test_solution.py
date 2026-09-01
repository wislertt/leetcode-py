import pytest

from leetcode_py import logged_test

from .helpers import assert_probability_of_heads, run_probability_of_heads
from .solution import Solution


class TestTossStrangeCoins:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prob, target, expected",
        [
            ([0.4], 1, 0.4),
            ([0.5, 0.5, 0.5, 0.5, 0.5], 0, 0.03125),
            ([0.5, 0.5, 0.5, 0.5, 0.5], 2, 0.3125),
            ([0.5, 0.5, 0.5, 0.5, 0.5], 5, 0.03125),
            ([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 4, 0.2734375),
            ([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 5, 0.24609375),
            ([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], 10, 0.0009765625),
            ([1.0, 1.0, 1.0], 3, 1.0),
            ([1.0, 1.0, 1.0], 0, 0.0),
            ([0.0, 0.0, 0.0], 0, 1.0),
            ([0.0, 1.0, 0.0], 1, 1.0),
            ([0.25, 0.25, 0.25, 0.25], 2, 0.2109375),
            ([0.9, 0.2, 0.1, 0.3], 2, 0.3674),
            ([0.7], 0, 0.3),
            ([0.3, 0.6, 0.9, 0.2], 3, 0.2304),
            ([0.125, 0.375, 0.625, 0.875], 3, 0.2412109375),
            ([0.125, 0.375, 0.625, 0.875], 4, 0.025634765625),
            (
                [0.8, 0.2, 0.5, 0.7, 0.9, 0.3, 0.6, 0.2, 0.5, 0.7, 0.7, 0.2, 0.5, 0.3],
                10,
                0.05371541936,
            ),
        ],
    )
    def test_probability_of_heads(self, prob: list[float], target: int, expected: float):
        result = run_probability_of_heads(Solution, prob, target)
        assert_probability_of_heads(result, expected)
