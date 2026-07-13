# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_end, run_min_end
from solution import Solution

# %%
# Example test case
n = 3
x = 4
expected = 6

# %%
result = run_min_end(Solution, n, x)
result

# %%
assert_min_end(result, expected)
