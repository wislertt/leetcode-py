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
from helpers import assert_smallest_good_base, run_smallest_good_base
from solution import Solution

# %%
# Example test case
n = "13"
expected = "3"

# %%
result = run_smallest_good_base(Solution, n)
result

# %%
assert_smallest_good_base(result, expected)
