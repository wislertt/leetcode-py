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
from helpers import assert_replace_elements, run_replace_elements
from solution import Solution

# %%
# Example test case
arr = [17, 18, 5, 4, 6, 1]
expected = [18, 6, 6, 6, 1, -1]

# %%
result = run_replace_elements(Solution, arr)
result

# %%
assert_replace_elements(result, expected)
