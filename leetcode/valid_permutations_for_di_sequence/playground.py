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
from helpers import assert_num_perms_di_sequence, run_num_perms_di_sequence
from solution import Solution

# %%
# Example test case
s = "DID"
expected = 5

# %%
result = run_num_perms_di_sequence(Solution, s)
result

# %%
assert_num_perms_di_sequence(result, expected)
