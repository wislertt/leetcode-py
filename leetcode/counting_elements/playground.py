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
from helpers import assert_count_elements, run_count_elements
from solution import Solution

# %%
# Example test case
arr: list[int] = [1, 2, 3]
expected = 2

# %%
result = run_count_elements(Solution, arr)
result

# %%
assert_count_elements(result, expected)
