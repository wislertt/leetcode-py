import pytest

from leetcode_py import logged_test

from .helpers import assert_contain_virus, run_contain_virus
from .solution import Solution


class TestContainVirus:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "is_infected, expected",
        [
            (
                [
                    [0, 1, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ],
                10,
            ),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 4),
            (
                [
                    [1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 0, 0, 0, 0, 0],
                ],
                13,
            ),
            ([[0]], 0),
            ([[1]], 0),
            ([[1, 1], [1, 1]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[1, 0], [0, 0]], 2),
            ([[1, 1, 0], [0, 0, 0]], 3),
            ([[0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1]], 9),
            ([[1, 0, 0, 0]], 1),
            ([[0, 1], [0, 0]], 2),
            ([[1, 0], [1, 1], [0, 0]], 4),
            ([[0, 1, 0, 1]], 2),
            ([[0, 1], [0, 1], [0, 1], [0, 0]], 4),
            ([[1, 1, 1], [1, 1, 0]], 2),
        ],
    )
    def test_contain_virus(self, is_infected: list[list[int]], expected: int):
        result = run_contain_virus(Solution, is_infected)
        assert_contain_virus(result, expected)
