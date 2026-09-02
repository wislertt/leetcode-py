import pytest

from leetcode_py import logged_test

from .helpers import assert_find_all_recipes, run_find_all_recipes
from .solution import Solution


class TestFindAllPossibleRecipesFromGivenSupplies:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "recipes, ingredients, supplies, expected",
        [
            (["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"], ["bread"]),
            (["b", "s"], [["y", "f"], ["b", "m"]], ["y", "f", "m"], ["b", "s"]),
            (
                ["b", "s", "g"],
                [["y", "f"], ["b", "m"], ["s", "m", "b"]],
                ["y", "f", "m"],
                ["b", "g", "s"],
            ),
            (["cake"], [["flour", "sugar"]], ["flour"], []),
            (["a", "b"], [["b"], ["a"]], ["c"], []),
            (["aa"], [["aa"]], ["zz"], []),
            (["soup", "stew"], [["salt", "water"], ["soup", "beef"]], ["salt", "pepper"], []),
            (["z", "y", "x", "w"], [["s"], ["z"], ["y", "s"], ["nope"]], ["s"], ["x", "y", "z"]),
            (["d", "e"], [["sa", "sb"], ["sa"]], ["sa", "sb"], ["d", "e"]),
            (["t", "p", "s"], [["h"], ["d", "h"], ["h", "s"]], ["h", "d", "i"], ["p", "t"]),
            (["k", "t", "l"], [["l", "g"], ["k"], ["a"]], ["a", "i", "g"], ["k", "l", "t"]),
            (["t", "p"], [["a"], ["t", "a", "c"]], ["c", "a"], ["p", "t"]),
            (["q", "l", "n"], [["l"], ["n"], ["q", "c"]], ["c"], []),
            (["l"], [["l", "a"]], ["a"], []),
            (["o", "m", "s"], [["s"], ["b", "m", "f"], ["b", "s"]], ["f", "b"], []),
            (
                ["l", "t", "s", "p"],
                [["i", "s", "l"], ["i", "p"], ["p", "s", "i"], ["p", "s", "t"]],
                ["i"],
                [],
            ),
            (["k"], [["a", "d"]], ["a", "e", "d"], ["k"]),
            (["n", "r", "m"], [["b", "m", "n"], ["b", "r", "m"], ["n", "r"]], ["f", "b"], []),
            (["t"], [["t", "h"]], ["a", "e", "j", "h"], []),
        ],
    )
    def test_find_all_recipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
        expected: list[str],
    ):
        result = run_find_all_recipes(Solution, recipes, ingredients, supplies)
        assert_find_all_recipes(result, expected)
