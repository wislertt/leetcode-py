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
from helpers import assert_map_sum, run_map_sum
from solution import MapSum

# %%
# Example test case
operations = ["MapSum", "insert", "sum", "insert", "sum"]
inputs = [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
expected = [None, None, 3, None, 5]

# %%
result, map_sum = run_map_sum(MapSum, operations, inputs)
print(result)
map_sum

# %%
assert_map_sum(result, expected)
