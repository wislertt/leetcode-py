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
from helpers import assert_max_chunks_to_sorted, run_max_chunks_to_sorted
from solution import Solution

# %%
# Example test case
arr = [4, 3, 2, 1, 0]
expected = 1

# %%
result = run_max_chunks_to_sorted(Solution, arr)
result

# %%
assert_max_chunks_to_sorted(result, expected)
