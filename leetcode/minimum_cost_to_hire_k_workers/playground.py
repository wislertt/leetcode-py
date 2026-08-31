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
from helpers import assert_mincost_to_hire_workers, run_mincost_to_hire_workers
from solution import Solution

# %%
# Example test case
quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
expected = 105.0

# %%
result = run_mincost_to_hire_workers(Solution, quality, wage, k)
result

# %%
assert_mincost_to_hire_workers(result, expected)
