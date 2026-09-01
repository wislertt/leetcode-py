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
from helpers import assert_best_closing_time, run_best_closing_time
from solution import Solution

# %%
# Example test case
customers = "YYNY"
expected = 2

# %%
result = run_best_closing_time(Solution, customers)
result

# %%
assert_best_closing_time(result, expected)
