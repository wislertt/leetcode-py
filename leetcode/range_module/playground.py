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
from helpers import assert_range_module, run_range_module
from solution import RangeModule

# %%
# Example test case
operations = ["RangeModule", "add_range", "remove_range", "query_range", "query_range"]
inputs = [[], [10, 20], [14, 16], [10, 14], [13, 15]]
expected = [None, None, None, True, False]

# %%
result, module = run_range_module(RangeModule, operations, inputs)
print(result)
module

# %%
assert_range_module(result, expected)
