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
from helpers import assert_find_all_recipes, run_find_all_recipes
from solution import Solution

# %%
# Example test case
recipes = ["bread", "sandwich"]
ingredients = [["yeast", "flour"], ["bread", "meat"]]
supplies = ["yeast", "flour", "meat"]
expected = ["bread", "sandwich"]

# %%
result = run_find_all_recipes(Solution, recipes, ingredients, supplies)
print(result)
result

# %%
assert_find_all_recipes(result, expected)
