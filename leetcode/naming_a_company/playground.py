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
from helpers import assert_distinct_names, run_distinct_names
from solution import Solution

# %%
# Example test case
ideas: list[str] = ["coffee", "donuts", "time", "toffee"]
expected = 6

# %%
result = run_distinct_names(Solution, ideas)
result

# %%
assert_distinct_names(result, expected)
