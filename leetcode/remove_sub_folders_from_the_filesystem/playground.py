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
from helpers import assert_remove_subfolders, run_remove_subfolders
from solution import Solution

# %%
# Example test case
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
expected = ["/a", "/c/d", "/c/f"]

# %%
result = run_remove_subfolders(Solution, folder)
result

# %%
assert_remove_subfolders(result, expected)
