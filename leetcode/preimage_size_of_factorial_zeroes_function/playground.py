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
from helpers import assert_preimage_size_fzf, run_preimage_size_fzf
from solution import Solution

# %%
# Example test case
k = 0
expected = 5

# %%
result = run_preimage_size_fzf(Solution, k)
result

# %%
assert_preimage_size_fzf(result, expected)
