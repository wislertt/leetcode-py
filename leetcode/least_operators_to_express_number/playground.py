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
from helpers import assert_least_ops_express_target, run_least_ops_express_target
from solution import Solution

# %%
# Example test case
x = 3
target = 19
expected = 5

# %%
result = run_least_ops_express_target(Solution, x, target)
result

# %%
assert_least_ops_express_target(result, expected)
