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
from helpers import assert_dest_city, run_dest_city
from solution import Solution

# %%
# Example test case
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
expected = "Sao Paulo"

# %%
result = run_dest_city(Solution, paths)
result

# %%
assert_dest_city(result, expected)
