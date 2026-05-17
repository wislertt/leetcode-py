# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_eval_rpn, run_eval_rpn
from solution import Solution

# %%
# Example test case
tokens = ["2", "1", "+", "3", "*"]
expected = 9

# %%
result = run_eval_rpn(Solution, tokens)
result

# %%
assert_eval_rpn(result, expected)
