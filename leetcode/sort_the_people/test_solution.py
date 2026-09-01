import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_people, run_sort_people
from .solution import Solution


class TestSortThePeople:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "names, heights, expected",
        [
            (["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
            (["Alice", "Bob", "Bob"], [155, 185, 150], ["Bob", "Alice", "Bob"]),
            (["A"], [1], ["A"]),
            (["Zed"], [100000], ["Zed"]),
            (["a", "b"], [2, 1], ["a", "b"]),
            (["a", "b"], [1, 2], ["b", "a"]),
            (["Tom", "Sue", "Ann", "Bob"], [170, 165, 180, 150], ["Ann", "Tom", "Sue", "Bob"]),
            (["Al", "Be", "Cy", "Di", "Ed"], [5, 4, 3, 2, 1], ["Al", "Be", "Cy", "Di", "Ed"]),
            (["Aa", "Bb", "Cc"], [7, 9, 8], ["Bb", "Cc", "Aa"]),
            (
                ["Neo", "Tank", "Apoc", "Dozer"],
                [100, 300, 400, 200],
                ["Apoc", "Tank", "Dozer", "Neo"],
            ),
            (["xy", "ab", "qq", "zz", "mm"], [11, 22, 44, 33, 55], ["mm", "qq", "zz", "ab", "xy"]),
            (["Kim", "Lee", "Park", "Choi"], [60, 10, 50, 20], ["Kim", "Park", "Choi", "Lee"]),
            (["One"], [99999], ["One"]),
            (["An", "Bo", "Cy", "Di", "Ed"], [7, 6, 5, 4, 3], ["An", "Bo", "Cy", "Di", "Ed"]),
        ],
    )
    def test_sort_people(self, names: list[str], heights: list[int], expected: list[str]):
        result = run_sort_people(Solution, names, heights)
        assert_sort_people(result, expected)
