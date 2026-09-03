import pytest

from leetcode_py import logged_test

from .helpers import assert_find_restaurant, run_find_restaurant
from .solution import Solution


class TestMinimumIndexSumOfTwoLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "list1, list2, expected",
        [
            (["a"], ["a"], ["a"]),
            (["a", "b"], ["b", "a"], ["a", "b"]),
            (["a", "b"], ["a", "b"], ["a"]),
            (["x", "y", "z"], ["z", "y", "x"], ["x", "y", "z"]),
            (["happy", "sad", "good"], ["sad", "happy", "good"], ["happy", "sad"]),
            (["Shogun", "KFC"], ["KFC", "Shogun"], ["KFC", "Shogun"]),
            (["Shogun", "Tapioca", "KFC"], ["Piatti", "Shogun", "KFC"], ["Shogun"]),
            (["b", "a", "c"], ["a", "b", "c"], ["a", "b"]),
            (["w"], ["w", "v"], ["w"]),
            (["p", "q", "r"], ["s", "p", "t"], ["p"]),
            (["aa", "bb", "cc", "dd"], ["dd", "cc", "bb", "aa"], ["aa", "bb", "cc", "dd"]),
            (["alpha", "beta"], ["beta", "gamma", "alpha"], ["beta"]),
            (["ice cream", "hot dog"], ["hot dog", "tea"], ["hot dog"]),
            (["milk tea", "coffee", "juice"], ["juice", "coffee"], ["coffee", "juice"]),
            (["k", "l"], ["m", "n", "o", "k"], ["k"]),
            (["ab", "cd", "ef"], ["xy", "ef"], ["ef"]),
            (["tea", "coke", "water"], ["water", "coke", "tea"], ["coke", "tea", "water"]),
            (["a", "b", "c", "d", "e", "f", "g", "h"], ["h", "g", "f", "e"], ["e", "f", "g", "h"]),
        ],
    )
    def test_find_restaurant(self, list1: list[str], list2: list[str], expected: list[str]):
        result = run_find_restaurant(Solution, list1, list2)
        assert_find_restaurant(result, expected)
