# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_network_delay_time, run_network_delay_time
from solution import Solution

# %%
# Example test case
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
expected = 2

# %%
result = run_network_delay_time(Solution, times, n, k)
result

# %%
assert_network_delay_time(result, expected)
