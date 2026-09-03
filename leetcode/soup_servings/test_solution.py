import pytest

from leetcode_py import logged_test

from .helpers import assert_soup_servings, run_soup_servings
from .solution import Solution


class TestSoupServings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0.5),
            (1, 0.625),
            (25, 0.625),
            (50, 0.625),
            (60, 0.65625),
            (75, 0.65625),
            (100, 0.71875),
            (125, 0.7421875),
            (150, 0.7578125),
            (175, 0.78515625),
            (200, 0.796875),
            (250, 0.82763671875),
            (300, 0.8521728515625),
            (500, 0.916344165802002),
            (1000, 0.9765650521094358),
            (2000, 0.9977163163248763),
            (5000, 1.0),
            (1000000000, 1.0),
        ],
    )
    def test_soup_servings(self, n: int, expected: float):
        result = run_soup_servings(Solution, n)
        assert_soup_servings(result, expected)
