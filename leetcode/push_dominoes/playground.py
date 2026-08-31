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
from helpers import assert_push_dominoes, run_push_dominoes
from solution import Solution

# %%
# Example test case
dominoes = "RR.L"
expected = "RR.L"

# %%
result = run_push_dominoes(Solution, dominoes)
result

# %%
assert_push_dominoes(result, expected)
