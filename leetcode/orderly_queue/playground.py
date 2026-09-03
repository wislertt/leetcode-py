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
from helpers import assert_orderly_queue, run_orderly_queue
from solution import Solution

# %%
# Example test case
s = "cba"
k = 1
expected = "acb"

# %%
result = run_orderly_queue(Solution, s, k)
result

# %%
assert_orderly_queue(result, expected)
