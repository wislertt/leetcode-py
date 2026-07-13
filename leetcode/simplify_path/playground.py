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
from helpers import assert_simplify_path, run_simplify_path
from solution import Solution

# %%
# Example test case
path = "/home/"
expected = "/home"

# %%
result = run_simplify_path(Solution, path)
result

# %%
assert_simplify_path(result, expected)
