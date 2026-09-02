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
from helpers import assert_pseudo_palindromic_paths, run_pseudo_palindromic_paths
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 3, 1, 3, 1, None, 1]
expected: int = 2

# %%
result = run_pseudo_palindromic_paths(Solution, root_list)
result

# %%
assert_pseudo_palindromic_paths(result, expected)
