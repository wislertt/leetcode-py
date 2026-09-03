import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_path_all_keys, run_shortest_path_all_keys
from .solution import Solution


class TestTestShortestPathToGetAllKeys:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            (["@.a..", "###.#", "b.A.B"], 8),
            (["@..aA", "..B#.", "....b"], 6),
            (["@Aa"], -1),
            (["@aA"], 1),
            (["@.a.A"], 2),
            (["@#aA"], -1),
            (["Aa@"], 1),
            (["@aAbB"], 3),
            (["@aA.b.B"], 4),
            (["@aAbBcC"], 5),
            (["@.a.Ab.B"], 5),
            (["@.a.AB", "#..b.."], 4),
            (["@.a.AB", "b....."], 4),
            (["@abcdefABCDEF"], 6),
            (["@f.a.d.b.e.cABCDEF"], 11),
            (["@..a..b..c", "ABC......."], 9),
            (["@#a#b#c", ".A.B.C."], -1),
            (["@.a.", "#...", "A.bB"], 4),
            ([".#A.", "#...", ".#..", ".#@a", "#..#"], 1),
            (["b.", "A@", "aB"], 6),
            (["..#.C", "....B", "Aac..", "##.@b"], 5),
            ([".ab", "..c", ".CB", "@.A"], 6),
        ],
    )
    def test_shortest_path_all_keys(self, grid: list[str], expected: int):
        result = run_shortest_path_all_keys(Solution, grid)
        assert_shortest_path_all_keys(result, expected)
