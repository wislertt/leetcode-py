import pytest

from leetcode_py import logged_test

from .helpers import assert_food_ratings, run_food_ratings
from .solution import FoodRatings


class TestDesignAFoodRatingSystem:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                ],
                [
                    [
                        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                        [9, 12, 8, 15, 14, 7],
                    ],
                    ["korean"],
                    ["japanese"],
                    ["sushi", 16],
                    ["japanese"],
                    ["ramen", 16],
                    ["japanese"],
                ],
                [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
            ),
            (
                ["FoodRatings", "highest_rated", "highest_rated"],
                [[["maki", "udon", "taco"], ["jp", "jp", "mx"], [10, 10, 4]], ["jp"], ["mx"]],
                [None, "maki", "taco"],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                ],
                [
                    [["soba", "ramen"], ["jp", "jp"], [5, 9]],
                    ["jp"],
                    ["soba", 9],
                    ["jp"],
                    ["ramen", 3],
                    ["jp"],
                ],
                [None, "ramen", None, "ramen", None, "soba"],
            ),
            (
                ["FoodRatings", "highest_rated", "highest_rated"],
                [[["soup"], ["warm"], [3]], ["warm"], ["warm"]],
                [None, "soup", "soup"],
            ),
            (
                ["FoodRatings", "highest_rated", "change_rating", "highest_rated", "highest_rated"],
                [
                    [["cake", "pie", "tart"], ["sweet", "sweet", "sweet"], [8, 5, 2]],
                    ["sweet"],
                    ["cake", 1],
                    ["sweet"],
                    ["sweet"],
                ],
                [None, "cake", None, "pie", "pie"],
            ),
            (
                ["FoodRatings", "highest_rated", "change_rating", "highest_rated"],
                [[["naan", "pita"], ["bread", "bread"], [7, 7]], ["bread"], ["naan", 7], ["bread"]],
                [None, "naan", None, "naan"],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "highest_rated",
                ],
                [
                    [
                        ["falafel", "hummus", "salsa", "queso"],
                        ["mid", "mid", "lat", "lat"],
                        [6, 9, 8, 3],
                    ],
                    ["mid"],
                    ["lat"],
                    ["queso", 12],
                    ["lat"],
                    ["queso", 1],
                    ["lat"],
                    ["mid"],
                ],
                [None, "hummus", "salsa", None, "queso", None, "salsa", "hummus"],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                ],
                [
                    [["tofu", "seaweed"], ["vegan", "vegan"], [2, 20]],
                    ["vegan"],
                    ["tofu", 21],
                    ["vegan"],
                    ["tofu", 20],
                    ["vegan"],
                ],
                [None, "seaweed", None, "tofu", None, "seaweed"],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "highest_rated",
                ],
                [
                    [["aa", "ab", "ba", "bb"], ["c", "c", "c", "c"], [4, 6, 6, 2]],
                    ["c"],
                    ["bb", 9],
                    ["c"],
                    ["aa", 9],
                    ["c"],
                    ["bb", 9],
                    ["c"],
                    ["c"],
                ],
                [None, "ab", None, "bb", None, "aa", None, "aa", "aa"],
            ),
            (
                [
                    "FoodRatings",
                    "change_rating",
                    "change_rating",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                ],
                [
                    [["ba", "dd", "bb", "cc"], ["y", "x", "x", "y"], [63, 99, 67, 33]],
                    ["dd", 97],
                    ["dd", 76],
                    ["ba", 28],
                    ["x"],
                    ["cc", 47],
                    ["y"],
                ],
                [None, None, None, None, "dd", None, "cc"],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "highest_rated",
                    "change_rating",
                ],
                [[["ba", "bb"], ["x", "y"], [1, 37]], ["x"], ["bb", 97], ["x"], ["y"], ["bb", 51]],
                [None, "ba", None, "ba", "bb", None],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "highest_rated",
                    "highest_rated",
                    "change_rating",
                    "change_rating",
                ],
                [[["cc", "ba"], ["z", "y"], [18, 84]], ["z"], ["y"], ["y"], ["cc", 14], ["cc", 61]],
                [None, "cc", "ba", "ba", None, None],
            ),
            (
                [
                    "FoodRatings",
                    "highest_rated",
                    "change_rating",
                    "change_rating",
                    "highest_rated",
                    "change_rating",
                    "highest_rated",
                    "highest_rated",
                ],
                [
                    [["ba", "dd", "cc", "bb"], ["z", "x", "z", "x"], [31, 59, 26, 100]],
                    ["x"],
                    ["cc", 49],
                    ["cc", 29],
                    ["z"],
                    ["dd", 4],
                    ["z"],
                    ["x"],
                ],
                [None, "bb", None, None, "ba", None, "ba", "bb"],
            ),
            (
                ["FoodRatings", "change_rating", "change_rating", "change_rating", "highest_rated"],
                [
                    [["ab", "dd", "ba", "cc"], ["x", "y", "y", "y"], [41, 60, 27, 42]],
                    ["ab", 65],
                    ["ba", 37],
                    ["cc", 91],
                    ["y"],
                ],
                [None, None, None, None, "cc"],
            ),
            (
                ["FoodRatings", "highest_rated", "highest_rated", "change_rating", "change_rating"],
                [[["dd", "ba"], ["y", "z"], [88, 36]], ["z"], ["y"], ["ba", 62], ["ba", 89]],
                [None, "ba", "dd", None, None],
            ),
        ],
    )
    def test_food_ratings(
        self, operations: list[str], inputs: list[list], expected: list[str | None]
    ):
        result, _ = run_food_ratings(FoodRatings, operations, inputs)
        assert_food_ratings(result, expected)
