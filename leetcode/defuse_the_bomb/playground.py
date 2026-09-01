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
from helpers import assert_decrypt, run_decrypt
from solution import Solution

# %%
# Example test case
code = [5, 7, 1, 4]
k = 3
expected = [12, 10, 16, 13]

# %%
result = run_decrypt(Solution, code, k)
result

# %%
assert_decrypt(result, expected)
