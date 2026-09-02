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
from helpers import assert_random_pick_index, run_random_pick_index
from solution import Solution

# %%
# Example test case
operations = ["Solution", "pick", "pick", "pick"]
inputs = [[[1, 2, 3, 3, 3]], [3], [1], [3]]
expected = [[None], [2, 3, 4], [0], [2, 3, 4]]

# %%
result = run_random_pick_index(Solution, operations, inputs)
print(result)
result

# %%
assert_random_pick_index(result, expected)
