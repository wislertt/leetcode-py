# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_food_ratings, run_food_ratings
from solution import FoodRatings

# %%
# Example test case
operations = ["FoodRatings", "highest_rated", "highest_rated", "change_rating", "highest_rated"]
inputs = [
    [["kimchi", "miso"], ["korean", "japanese"], [9, 12]],
    [["korean"]],
    [["japanese"]],
    [["miso", 15]],
    [["japanese"]],
]
expected = [None, "kimchi", "miso", None, "miso"]

# %%
result, system = run_food_ratings(FoodRatings, operations, inputs)
print(result)
system

# %%
assert_food_ratings(result, expected)
