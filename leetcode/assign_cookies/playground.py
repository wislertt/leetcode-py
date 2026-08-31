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
from helpers import assert_find_content_children, run_find_content_children
from solution import Solution

# %%
# Example test case
g = [1, 2, 3]
s = [1, 1]
expected = 1

# %%
result = run_find_content_children(Solution, g, s)
result

# %%
assert_find_content_children(result, expected)
