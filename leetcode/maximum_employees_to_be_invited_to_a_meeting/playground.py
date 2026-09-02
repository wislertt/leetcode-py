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
from helpers import assert_maximum_invitations, run_maximum_invitations
from solution import Solution

# %%
# Example test case
favorite = [3, 0, 1, 4, 1]
expected = 4

# %%
result = run_maximum_invitations(Solution, favorite)
result

# %%
assert_maximum_invitations(result, expected)
