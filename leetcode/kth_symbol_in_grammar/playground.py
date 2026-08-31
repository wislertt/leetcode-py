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
from helpers import assert_kth_grammar, run_kth_grammar
from solution import Solution

# %%
# Example test case
n = 1
k = 1
expected = 0

# %%
result = run_kth_grammar(Solution, n, k)
result

# %%
assert_kth_grammar(result, expected)
