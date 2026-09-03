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
from helpers import assert_find_replace_string, run_find_replace_string
from solution import Solution

# %%
# Example test case
s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
expected = "eeebffff"

# %%
result = run_find_replace_string(Solution, s, indices, sources, targets)
result

# %%
assert_find_replace_string(result, expected)
