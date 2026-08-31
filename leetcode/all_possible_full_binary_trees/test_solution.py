import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_all_possible_fbt,
    assert_all_possible_fbt_solution_count,
    run_all_possible_fbt,
)
from .solution import Solution


class TestAllPossibleFullBinaryTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, [[0]]),
            (3, [[0, 0, 0]]),
            (5, [[0, 0, 0, None, None, 0, 0], [0, 0, 0, 0, 0]]),
            (
                7,
                [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, None, None, 0, 0],
                    [0, 0, 0, None, None, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
                    [0, 0, 0, None, None, 0, 0, None, None, 0, 0],
                ],
            ),
        ],
    )
    def test_all_possible_fbt(self, n: int, expected: list[list[int | None]]):
        result = run_all_possible_fbt(Solution, n)
        assert_all_possible_fbt(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "n, expected_count",
        [(9, 14), (11, 42), (13, 132), (15, 429), (17, 1430), (19, 4862), (21, 16796), (23, 58786)],
    )
    def test_all_possible_fbt_solution_count(self, n: int, expected_count: int):
        result = run_all_possible_fbt(Solution, n)
        assert_all_possible_fbt_solution_count(result, expected_count)
